"""Hermes HQ data models."""

from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Any


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass(frozen=True, slots=True)
class MetricPoint:
    name: str
    current: str
    target: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class InitiativeCard:
    initiative_id: str
    name: str
    stage: str = "explore"
    target_customer: str = ""
    value_proposition: str = ""
    decision_state: str = "pending"
    metrics: tuple[MetricPoint, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["metrics"] = [metric.to_dict() for metric in self.metrics]
        return payload


@dataclass(frozen=True, slots=True)
class DecisionLogEntry:
    initiative_id: str
    decision: str
    actor: str
    rationale: str
    source: str
    follow_up: str = ""
    timestamp: str = field(default_factory=_utc_now_iso)
    previous_entry_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class ReviewSnapshot:
    initiative_id: str
    state: str
    summary: str
    action_required: str = ""
    timestamp: str = field(default_factory=_utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
