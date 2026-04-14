from pathlib import Path


def test_review_loop_exists():
    assert Path("docs/hq/review-loop.md").exists()


def test_review_loop_mentions_states():
    text = Path("docs/hq/review-loop.md").read_text()
    for state in ["pending", "reviewing", "approved", "rework", "blocked", "archived"]:
        assert state in text
