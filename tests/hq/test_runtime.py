from pathlib import Path

import pytest

from gateway.config import Platform
from gateway.session import SessionSource
from hq.models import DecisionLogEntry, InitiativeCard, MetricPoint, ReviewSnapshot
from hq.storage import (
    append_decision_log,
    append_metric_record,
    build_initiative_id,
    ensure_hq_dirs,
    get_hq_home,
    record_gateway_intake,
    write_initiative_card,
    write_review_snapshot,
)


def test_get_hq_home_respects_hermes_home(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    assert get_hq_home() == tmp_path / ".hermes" / "hq"


def test_ensure_hq_dirs_creates_expected_subdirs(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    home = ensure_hq_dirs()
    assert home == tmp_path / ".hermes" / "hq"
    for subdir in ["decision-log", "metrics", "initiatives", "reviews"]:
        assert (home / subdir).is_dir()


def test_write_initiative_card_and_review_snapshot(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    card = InitiativeCard(
        initiative_id="bd-ai-trend-ray",
        name="AI Trend Ray",
        stage="build",
        target_customer="Discord users",
        value_proposition="Summarize and route trend signals",
        metrics=(MetricPoint(name="throughput", current="3/day", target="10/day"),),
    )
    card_path = write_initiative_card(card)
    assert card_path == tmp_path / ".hermes" / "hq" / "initiatives" / "bd-ai-trend-ray.json"
    payload = card_path.read_text(encoding="utf-8")
    assert '"initiative_id": "bd-ai-trend-ray"' in payload
    assert '"metrics"' in payload

    snapshot = ReviewSnapshot(
        initiative_id="bd-ai-trend-ray",
        state="reviewing",
        summary="Needs baseline metrics",
        action_required="Add comparison window",
    )
    review_path = write_review_snapshot(snapshot)
    assert review_path == tmp_path / ".hermes" / "hq" / "reviews" / "bd-ai-trend-ray.json"
    assert '"state": "reviewing"' in review_path.read_text(encoding="utf-8")


def test_append_logs_are_jsonl_and_append_only(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    first = append_decision_log(
        DecisionLogEntry(
            initiative_id="bd-ai-trend-ray",
            decision="approved",
            actor="Hermes",
            rationale="Good fit",
            source="Discord",
            follow_up="Create queue",
        )
    )
    second = append_decision_log(
        DecisionLogEntry(
            initiative_id="bd-ai-trend-ray",
            decision="rework",
            actor="Hermes",
            rationale="Need narrower scope",
            source="Discord",
            follow_up="Reduce intake surface",
        )
    )
    assert first == second
    lines = first.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert '"decision": "approved"' in lines[0]
    assert '"decision": "rework"' in lines[1]

    metrics_path = append_metric_record(
        {
            "initiative_id": "bd-ai-trend-ray",
            "stage": "review",
            "decision_count": 2,
            "review_cycles": 1,
            "latency_ms": 1842,
            "status": "approved",
        }
    )
    assert metrics_path == tmp_path / ".hermes" / "hq" / "metrics" / "metrics.jsonl"
    assert '"latency_ms": 1842' in metrics_path.read_text(encoding="utf-8")


def test_record_gateway_intake_writes_hq_artifacts(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    source = SessionSource(
        platform=Platform.DISCORD,
        chat_id="1493230645776748635",
        chat_name="Ray & Hermes 인프라 개선",
        chat_type="thread",
        user_id="123",
        user_name="루카스",
        thread_id="1493230645776748635",
    )

    initiative_id = build_initiative_id(source, "discord-thread-1493230645776748635")
    assert initiative_id == "discord-thread-1493230645776748635"

    result = record_gateway_intake(
        source,
        "discord-thread-1493230645776748635",
        "BD 파이프라인부터 차례대로 연결해줘",
        session_id="session-abc",
        message_id="msg-1",
        is_new_session=True,
    )

    assert set(result) == {"initiative_card", "review_snapshot", "metric_record"}
    assert result["initiative_card"].exists()
    assert result["review_snapshot"].exists()
    assert result["metric_record"].exists()

    card_text = result["initiative_card"].read_text(encoding="utf-8")
    assert '"initiative_id": "discord-thread-1493230645776748635"' in card_text
    assert '"decision_state": "pending"' in card_text
    assert '"latest_message_preview": "BD 파이프라인부터 차례대로 연결해줘"' in card_text

    review_text = result["review_snapshot"].read_text(encoding="utf-8")
    assert '"state": "pending"' in review_text
    assert '"action_required": "Review intake"' in review_text

    metric_text = result["metric_record"].read_text(encoding="utf-8")
    assert '"status": "pending"' in metric_text
    assert '"session_id": "session-abc"' in metric_text
