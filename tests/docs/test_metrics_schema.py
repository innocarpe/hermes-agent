from pathlib import Path


def test_metrics_schema_exists():
    assert Path("docs/hq/metrics-schema.md").exists()


def test_metrics_schema_mentions_shared_dimensions():
    text = Path("docs/hq/metrics-schema.md").read_text()
    for key in ["initiative_id", "stage", "decision_count", "review_cycles", "latency_ms", "status"]:
        assert key in text
