from pathlib import Path


def test_decision_log_exists():
    assert Path("docs/hq/decision-log.md").exists()


def test_decision_log_is_append_only_by_policy():
    text = Path("docs/hq/decision-log.md").read_text()
    assert "append-only" in text
    for field in ["timestamp", "initiative_id", "decision", "actor", "rationale", "source", "follow_up"]:
        assert field in text
