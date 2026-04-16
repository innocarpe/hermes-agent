from cli import load_cli_config
from hermes_cli.config import DEFAULT_CONFIG


def test_goal_until_done_defaults_in_cli_config():
    config = load_cli_config()
    assert "goal_until_done" in config
    assert config["goal_until_done"]["enabled"] is True
    assert config["goal_until_done"]["default_max_attempts"] >= 1


def test_goal_until_done_defaults_in_main_config():
    assert "goal_until_done" in DEFAULT_CONFIG
    assert DEFAULT_CONFIG["goal_until_done"]["enabled"] is True
    assert DEFAULT_CONFIG["goal_until_done"]["default_max_idle_seconds"] == 600
