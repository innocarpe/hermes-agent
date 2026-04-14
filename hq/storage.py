"""File-backed persistence for Hermes HQ artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from hermes_constants import get_hermes_home

from gateway.session import SessionSource

from .models import DecisionLogEntry, InitiativeCard, MetricPoint, ReviewSnapshot


def get_hq_home() -> Path:
    return get_hermes_home() / "hq"


def ensure_hq_dirs() -> Path:
    home = get_hq_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "decision-log").mkdir(exist_ok=True)
    (home / "metrics").mkdir(exist_ok=True)
    (home / "initiatives").mkdir(exist_ok=True)
    (home / "reviews").mkdir(exist_ok=True)
    return home


def _append_jsonl(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        handle.write("\n")
    return path


def _slugify(value: str, fallback: str = "initiative") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or fallback


def build_initiative_id(source: SessionSource, session_key: str) -> str:
    base = session_key or ""
    if not base:
        parts = [
            source.platform.value if source.platform else "unknown",
            source.chat_type or "chat",
            source.chat_id or "",
            source.thread_id or "",
            source.user_id or source.user_id_alt or "",
        ]
        base = "-".join(part for part in parts if part)
    return _slugify(base)


def write_initiative_card(card: InitiativeCard) -> Path:
    home = ensure_hq_dirs()
    path = home / "initiatives" / f"{card.initiative_id}.json"
    path.write_text(json.dumps(card.to_dict(), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return path


def append_decision_log(entry: DecisionLogEntry) -> Path:
    home = ensure_hq_dirs()
    path = home / "decision-log" / "decisions.jsonl"
    return _append_jsonl(path, entry.to_dict())


def append_metric_record(record: dict[str, Any]) -> Path:
    home = ensure_hq_dirs()
    path = home / "metrics" / "metrics.jsonl"
    return _append_jsonl(path, record)


def write_review_snapshot(snapshot: ReviewSnapshot) -> Path:
    home = ensure_hq_dirs()
    path = home / "reviews" / f"{snapshot.initiative_id}.json"
    path.write_text(json.dumps(snapshot.to_dict(), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return path


def record_gateway_intake(
    source: SessionSource,
    session_key: str,
    message_text: str,
    *,
    session_id: str = "",
    message_id: str | None = None,
    is_new_session: bool = False,
) -> dict[str, Path]:
    """Persist a gateway intake record to the HQ layer.

    This keeps the gateway's first contact with a message mirrored into the
    shared HQ artifacts: initiative card, review snapshot, and metrics.
    """
    initiative_id = build_initiative_id(source, session_key)
    preview = (message_text or "").strip().replace("\n", " ")[:160]
    name = source.chat_name or source.user_name or initiative_id
    target_customer = source.user_name or source.chat_name or source.chat_id
    decision_state = "pending" if is_new_session else "reviewing"
    stage = "review"
    card = InitiativeCard(
        initiative_id=initiative_id,
        name=name,
        stage=stage,
        target_customer=target_customer or "",
        value_proposition=preview,
        decision_state=decision_state,
        metrics=(MetricPoint(name="inbound_messages", current="1", target="ongoing"),),
        metadata={
            "platform": source.platform.value if source.platform else "",
            "chat_type": source.chat_type,
            "chat_id": source.chat_id,
            "thread_id": source.thread_id,
            "session_key": session_key,
            "session_id": session_id,
            "message_id": message_id,
            "latest_message_preview": preview,
        },
    )
    review = ReviewSnapshot(
        initiative_id=initiative_id,
        state=decision_state,
        summary=preview or "Inbound message received",
        action_required="Review intake" if is_new_session else "Continue review",
    )
    metric = {
        "initiative_id": initiative_id,
        "stage": stage,
        "decision_count": 0 if is_new_session else 1,
        "review_cycles": 0,
        "latency_ms": 0,
        "status": decision_state,
        "source_platform": source.platform.value if source.platform else "",
        "session_id": session_id,
        "message_id": message_id,
    }
    return {
        "initiative_card": write_initiative_card(card),
        "review_snapshot": write_review_snapshot(review),
        "metric_record": append_metric_record(metric),
    }
