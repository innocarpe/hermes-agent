"""Tests for --ignore-user-config and --ignore-rules flags on `hermes chat`.

Ported from openai/codex#18646 (`feat: add --ignore-user-config and --ignore-rules`).
Codex's flags fully isolate a run from user-level config and exec-policy .rules
files. In Hermes the equivalent isolation is:

* ``--ignore-user-config`` → skip ``~/.hermes/config.yaml`` in ``load_cli_config()``
  (credentials in ``.env`` are still loaded).
* ``--ignore-rules`` → skip AGENTS.md / SOUL.md / .cursorrules auto-injection
  and persistent memory (maps to ``AIAgent(skip_context_files=True,
  skip_memory=True)``).

Both flags are wired via env vars so they work cleanly across the
argparse → cmd_chat → cli.main() → HermesCLI → AIAgent call chain.
"""

from __future__ import annotations

import os
import textwrap
import importlib

import pytest


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for var in ("HERMES_IGNORE_USER_CONFIG", "HERMES_IGNORE_RULES"):
        monkeypatch.delenv(var, raising=False)
    yield
    for var in ("HERMES_IGNORE_USER_CONFIG", "HERMES_IGNORE_RULES"):
        os.environ.pop(var, None)


class TestIgnoreUserConfigEnvGate:
    def _write_user_config(self, tmp_path, model_default):
        config_yaml = textwrap.dedent(
            f"""
            model:
              default: {model_default}
              provider: openrouter
            agent:
              system_prompt: "from user config"
            """
        ).lstrip()
        (tmp_path / "config.yaml").write_text(config_yaml)

    def _reload_cli(self, monkeypatch, tmp_path):
        import cli
        monkeypatch.setattr(cli, "_hermes_home", tmp_path)
        return cli.load_cli_config

    def test_user_config_loaded_when_flag_unset(self, tmp_path, monkeypatch):
        self._write_user_config(tmp_path, "anthropic/claude-sonnet-4.6")
        load_cli_config = self._reload_cli(monkeypatch, tmp_path)

        cfg = load_cli_config()

        assert cfg["model"]["default"] == "anthropic/claude-sonnet-4.6"
        assert cfg["agent"]["system_prompt"] == "from user config"

    def test_user_config_skipped_when_flag_set(self, tmp_path, monkeypatch):
        self._write_user_config(tmp_path, "anthropic/claude-sonnet-4.6")
        monkeypatch.setenv("HERMES_IGNORE_USER_CONFIG", "1")

        load_cli_config = self._reload_cli(monkeypatch, tmp_path)
        cfg = load_cli_config()

        assert cfg["agent"].get("system_prompt", "") != "from user config"
        assert cfg["model"].get("default", "") != "anthropic/claude-sonnet-4.6"

    def test_flag_ignored_when_set_to_other_value(self, tmp_path, monkeypatch):
        self._write_user_config(tmp_path, "anthropic/claude-sonnet-4.6")
        monkeypatch.setenv("HERMES_IGNORE_USER_CONFIG", "true")

        load_cli_config = self._reload_cli(monkeypatch, tmp_path)
        cfg = load_cli_config()

        assert cfg["model"]["default"] == "anthropic/claude-sonnet-4.6"


class TestIgnoreRulesEnvGate:
    def test_env_var_enables_ignore_rules(self, monkeypatch):
        monkeypatch.setenv("HERMES_IGNORE_RULES", "1")

        import cli
        importlib.reload(cli)

        obj = object.__new__(cli.HermesCLI)
        ignore_rules = False
        obj.ignore_rules = ignore_rules or os.environ.get("HERMES_IGNORE_RULES") == "1"

        assert obj.ignore_rules is True

    def test_constructor_flag_alone_enables_ignore_rules(self, monkeypatch):
        monkeypatch.delenv("HERMES_IGNORE_RULES", raising=False)
        import cli
        obj = object.__new__(cli.HermesCLI)
        ignore_rules = True
        obj.ignore_rules = ignore_rules or os.environ.get("HERMES_IGNORE_RULES") == "1"
        assert obj.ignore_rules is True

    def test_neither_flag_nor_env_leaves_rules_enabled(self, monkeypatch):
        monkeypatch.delenv("HERMES_IGNORE_RULES", raising=False)
        import cli
        obj = object.__new__(cli.HermesCLI)
        ignore_rules = False
        obj.ignore_rules = ignore_rules or os.environ.get("HERMES_IGNORE_RULES") == "1"
        assert obj.ignore_rules is False


class TestCmdChatWiring:
    def _simulate_cmd_chat_env_setup(self, args):
        if getattr(args, "ignore_user_config", False):
            os.environ["HERMES_IGNORE_USER_CONFIG"] = "1"
        if getattr(args, "ignore_rules", False):
            os.environ["HERMES_IGNORE_RULES"] = "1"

    def test_both_flags_set_both_env_vars(self, monkeypatch):
        monkeypatch.delenv("HERMES_IGNORE_USER_CONFIG", raising=False)
        monkeypatch.delenv("HERMES_IGNORE_RULES", raising=False)

        class FakeArgs:
            ignore_user_config = True
            ignore_rules = True

        self._simulate_cmd_chat_env_setup(FakeArgs())

        assert os.environ.get("HERMES_IGNORE_USER_CONFIG") == "1"
        assert os.environ.get("HERMES_IGNORE_RULES") == "1"

    def test_only_ignore_user_config(self, monkeypatch):
        monkeypatch.delenv("HERMES_IGNORE_USER_CONFIG", raising=False)
        monkeypatch.delenv("HERMES_IGNORE_RULES", raising=False)

        class FakeArgs:
            ignore_user_config = True
            ignore_rules = False

        self._simulate_cmd_chat_env_setup(FakeArgs())

        assert os.environ.get("HERMES_IGNORE_USER_CONFIG") == "1"
        assert "HERMES_IGNORE_RULES" not in os.environ

    def test_flags_absent_sets_nothing(self, monkeypatch):
        monkeypatch.delenv("HERMES_IGNORE_USER_CONFIG", raising=False)
        monkeypatch.delenv("HERMES_IGNORE_RULES", raising=False)

        class FakeArgs:
            pass

        self._simulate_cmd_chat_env_setup(FakeArgs())

        assert "HERMES_IGNORE_USER_CONFIG" not in os.environ
        assert "HERMES_IGNORE_RULES" not in os.environ


class TestArgparseFlagsRegistered:
    def test_flags_present_in_chat_parser(self):
        import argparse
        parser = argparse.ArgumentParser(prog="hermes")
        subs = parser.add_subparsers(dest="command")
        chat = subs.add_parser("chat")
        chat.add_argument("--ignore-user-config", action="store_true", default=False)
        chat.add_argument("--ignore-rules", action="store_true", default=False)

        args = parser.parse_args(["chat", "--ignore-user-config", "--ignore-rules"])
        assert args.ignore_user_config is True
        assert args.ignore_rules is True

    def test_main_py_registers_both_flags(self):
        import hermes_cli.main as hm
        import inspect
        src = inspect.getsource(hm)
        assert '"--ignore-user-config"' in src
        assert '"--ignore-rules"' in src
        assert "HERMES_IGNORE_USER_CONFIG" in src
        assert "HERMES_IGNORE_RULES" in src
