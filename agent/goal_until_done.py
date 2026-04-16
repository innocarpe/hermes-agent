from __future__ import annotations

import json
import time
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

from hermes_constants import get_hermes_home


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class RetryPolicy:
    max_attempts: int = 3
    backoff_seconds: list[int] = field(default_factory=lambda: [0, 30, 120])


@dataclass
class GoalContract:
    goal: str
    done_when: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    non_goals: list[str] = field(default_factory=list)
    retry_policy: RetryPolicy | dict[str, Any] = field(default_factory=RetryPolicy)
    max_runtime_seconds: int = 3600
    max_idle_seconds: int = 600
    approval_policy: str = "pause"
    blocker_policy: str = "classify"

    def __post_init__(self) -> None:
        if isinstance(self.retry_policy, dict):
            self.retry_policy = RetryPolicy(
                max_attempts=int(self.retry_policy.get("max_attempts", 3)),
                backoff_seconds=list(self.retry_policy.get("backoff_seconds", [0, 30, 120])),
            )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GoalContract":
        payload = dict(data)
        retry = payload.get("retry_policy") or {}
        if isinstance(retry, RetryPolicy):
            retry_policy = retry
        else:
            retry_policy = RetryPolicy(
                max_attempts=int(retry.get("max_attempts", 3)),
                backoff_seconds=list(retry.get("backoff_seconds", [0, 30, 120])),
            )
        payload["retry_policy"] = retry_policy
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["retry_policy"] = asdict(self.retry_policy)
        return data


@dataclass
class AttemptRecord:
    attempt_index: int
    started_at: str
    finished_at: str
    result_summary: str
    classifier_label: str
    budget_used: int = 0
    idle_seconds: float = 0.0
    tool_failures: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AttemptRecord":
        return cls(**data)


@dataclass
class GoalRunState:
    run_id: str
    session_id: str
    contract: GoalContract
    status: str
    attempts_used: int = 0
    last_attempt_summary: str = ""
    last_blocker_type: str = ""
    next_action: str = ""
    updated_at: str = field(default_factory=_utcnow)
    attempts: list[AttemptRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GoalRunState":
        payload = dict(data)
        payload["contract"] = GoalContract.from_dict(payload["contract"])
        payload["attempts"] = [AttemptRecord.from_dict(a) for a in payload.get("attempts", [])]
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "session_id": self.session_id,
            "contract": self.contract.to_dict(),
            "status": self.status,
            "attempts_used": self.attempts_used,
            "last_attempt_summary": self.last_attempt_summary,
            "last_blocker_type": self.last_blocker_type,
            "next_action": self.next_action,
            "updated_at": self.updated_at,
            "attempts": [asdict(a) for a in self.attempts],
        }


def get_goals_home() -> Path:
    path = get_hermes_home() / "goals"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def save_goal_state(state: GoalRunState, path: Optional[Path] = None) -> Path:
    out = path or (get_goals_home() / f"{state.run_id}.json")
    _write_json_atomic(out, state.to_dict())
    return out


def load_goal_state(path_or_run_id: str | Path) -> GoalRunState:
    path = Path(path_or_run_id)
    if not path.exists():
        path = get_goals_home() / f"{path_or_run_id}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return GoalRunState.from_dict(data)


def _extract_final_response(result: Any) -> str:
    if isinstance(result, dict):
        return str(result.get("final_response") or result.get("response") or "").strip()
    return str(result or "").strip()


def _done_criteria_met(contract: GoalContract, result: Any) -> bool:
    if isinstance(result, dict) and result.get("completed") is True:
        return True
    final_response = _extract_final_response(result).lower()
    if not contract.done_when:
        return False
    for criterion in contract.done_when:
        text = str(criterion).strip().lower()
        if text and text not in final_response:
            return False
    return True


def classify_attempt_outcome(
    contract: GoalContract,
    result: Any = None,
    *,
    exception: Optional[BaseException] = None,
    idle_timeout: bool = False,
    budget_exhausted: bool = False,
    approval_required: bool = False,
    tool_failures: Optional[list[str]] = None,
) -> str:
    tool_failures = tool_failures or []
    if _done_criteria_met(contract, result):
        return "completed"
    if approval_required:
        return "approval_required"
    lowered_failures = " ".join(tool_failures).lower()
    if any(token in lowered_failures for token in ("permission denied", "approval", "clarify")):
        return "approval_required"
    if idle_timeout:
        return "wait_and_retry"
    if budget_exhausted:
        return "budget_exhausted"
    if exception is not None:
        return "retryable_failure"
    if tool_failures:
        return "retryable_failure"
    if isinstance(result, dict) and result.get("terminal_blocker"):
        return "terminal_blocker"
    return "retryable_failure"


def build_attempt_prompt(contract: GoalContract, attempt_index: int, previous_summary: str = "") -> str:
    parts = [
        f"[GOAL] {contract.goal}",
        "[DONE WHEN]",
    ]
    if contract.done_when:
        parts.extend(f"- {item}" for item in contract.done_when)
    else:
        parts.append("- Explicitly state when the goal is complete.")
    if contract.constraints:
        parts.append("[CONSTRAINTS]")
        parts.extend(f"- {item}" for item in contract.constraints)
    if contract.non_goals:
        parts.append("[NON-GOALS]")
        parts.extend(f"- {item}" for item in contract.non_goals)
    parts.append(f"[ATTEMPT] {attempt_index}")
    if previous_summary:
        parts.append("[PREVIOUS ATTEMPT SUMMARY]")
        parts.append(previous_summary)
    parts.append(
        "Work toward completion. If blocked, explain the blocker clearly and whether it is retryable, approval-required, or terminal."
    )
    return "\n".join(parts)


def run_until_done(
    contract: GoalContract | dict[str, Any],
    attempt_callback: Callable[[int, str], Any],
    *,
    session_id: str = "",
    state_path: Optional[Path] = None,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> GoalRunState:
    if isinstance(contract, dict):
        contract = GoalContract.from_dict(contract)
    run_id = uuid.uuid4().hex
    state = GoalRunState(
        run_id=run_id,
        session_id=session_id,
        contract=contract,
        status="running",
        next_action="start_attempt_1",
    )
    save_goal_state(state, state_path)
    started_monotonic = time.monotonic()
    previous_summary = ""

    for attempt_index in range(1, contract.retry_policy.max_attempts + 1):
        if contract.max_runtime_seconds > 0 and (time.monotonic() - started_monotonic) > contract.max_runtime_seconds:
            state.status = "terminal_blocker"
            state.last_blocker_type = "max_runtime_exceeded"
            state.next_action = "stop"
            state.updated_at = _utcnow()
            save_goal_state(state, state_path)
            return state

        attempt_started = _utcnow()
        result = None
        exc: Optional[BaseException] = None
        try:
            attempt_prompt = build_attempt_prompt(contract, attempt_index, previous_summary)
            result = attempt_callback(attempt_index, attempt_prompt)
        except BaseException as e:  # pragma: no cover - exercised via tests
            exc = e

        label = classify_attempt_outcome(
            contract,
            result,
            exception=exc,
            tool_failures=list((result or {}).get("tool_failures", [])) if isinstance(result, dict) else [],
        )
        summary = _extract_final_response(result) if exc is None else str(exc)
        record = AttemptRecord(
            attempt_index=attempt_index,
            started_at=attempt_started,
            finished_at=_utcnow(),
            result_summary=summary,
            classifier_label=label,
            budget_used=int((result or {}).get("activity", {}).get("budget_used", 0)) if isinstance(result, dict) else 0,
            idle_seconds=float((result or {}).get("activity", {}).get("idle_seconds", 0.0)) if isinstance(result, dict) else 0.0,
            tool_failures=list((result or {}).get("tool_failures", [])) if isinstance(result, dict) else [],
        )
        state.attempts.append(record)
        state.attempts_used = attempt_index
        state.last_attempt_summary = summary
        state.last_blocker_type = label if label != "completed" else ""
        state.updated_at = _utcnow()

        if label == "completed":
            state.status = "completed"
            state.next_action = "done"
            save_goal_state(state, state_path)
            return state
        if label == "approval_required":
            state.status = "approval_required"
            state.next_action = "await_approval"
            save_goal_state(state, state_path)
            return state
        if label == "terminal_blocker":
            state.status = "terminal_blocker"
            state.next_action = "stop"
            save_goal_state(state, state_path)
            return state

        state.status = label
        state.next_action = "retry"
        save_goal_state(state, state_path)
        previous_summary = summary
        backoff = 0
        if contract.retry_policy.backoff_seconds:
            idx = min(attempt_index - 1, len(contract.retry_policy.backoff_seconds) - 1)
            backoff = max(0, int(contract.retry_policy.backoff_seconds[idx]))
        if backoff:
            sleep_fn(backoff)

    state.status = "budget_exhausted"
    state.last_blocker_type = "budget_exhausted"
    state.next_action = "stop"
    state.updated_at = _utcnow()
    save_goal_state(state, state_path)
    return state
