from pathlib import Path
from unittest.mock import MagicMock, patch

from agent.goal_until_done import GoalContract, GoalRunState, save_goal_state
from cli import HermesCLI
from hermes_cli.commands import resolve_command


def _make_cli():
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.config = {}
    cli_obj.console = MagicMock()
    cli_obj.agent = None
    cli_obj.conversation_history = []
    cli_obj.session_id = "sess-123"
    cli_obj._pending_input = MagicMock()
    cli_obj._session_db = MagicMock()
    cli_obj._agent_running = False
    cli_obj._background_tasks = {}
    cli_obj._background_task_counter = 0
    cli_obj.max_turns = 90
    cli_obj.enabled_toolsets = []
    cli_obj.reasoning_config = None
    cli_obj.service_tier = None
    cli_obj._providers_only = None
    cli_obj._providers_ignore = None
    cli_obj._providers_order = None
    cli_obj._provider_sort = None
    cli_obj._provider_require_params = False
    cli_obj._provider_data_collection = None
    cli_obj._fallback_model = None
    cli_obj._app = None
    return cli_obj


def test_until_done_commands_registered():
    assert resolve_command("until-done") is not None
    assert resolve_command("goal-status") is not None
    assert resolve_command("goal-stop") is not None
    assert resolve_command("goal-resume") is not None
    assert resolve_command("goal-list") is not None
    assert resolve_command("ud").name == "until-done"


def test_process_command_dispatches_until_done():
    cli_obj = _make_cli()
    with patch.object(cli_obj, "_handle_until_done_command") as mock_handler:
        assert cli_obj.process_command("/until-done finish oauth") is True
    mock_handler.assert_called_once_with("/until-done finish oauth")


def test_process_command_dispatches_goal_status_stop_resume_and_list():
    cli_obj = _make_cli()
    with patch.object(cli_obj, "_handle_goal_status_command") as mock_status, \
         patch.object(cli_obj, "_handle_goal_stop_command") as mock_stop, \
         patch.object(cli_obj, "_handle_goal_resume_command") as mock_resume, \
         patch.object(cli_obj, "_handle_goal_list_command") as mock_list:
        assert cli_obj.process_command("/goal-status") is True
        assert cli_obj.process_command("/goal-stop") is True
        assert cli_obj.process_command("/goal-resume") is True
        assert cli_obj.process_command("/goal-list") is True
    mock_status.assert_called_once_with("/goal-status")
    mock_stop.assert_called_once_with("/goal-stop")
    mock_resume.assert_called_once_with("/goal-resume")
    mock_list.assert_called_once_with("/goal-list")


def test_goal_list_shows_runs_in_reverse_order(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    cli_obj = _make_cli()
    cli_obj._goal_runs = {
        "goal_1": {"goal": "first", "state": "completed", "state_path": str(tmp_path / "goal_1.json"), "thread": None, "last_summary": ""},
        "goal_2": {"goal": "second", "state": "approval_required", "state_path": str(tmp_path / "goal_2.json"), "thread": None, "last_summary": ""},
    }

    with patch("cli._cprint") as mock_cprint:
        cli_obj._handle_goal_list_command("/goal-list")

    printed = "\n".join(call.args[0] for call in mock_cprint.call_args_list)
    assert "goal_2" in printed
    assert "approval_required" in printed
    assert "goal_1" in printed


def test_goal_status_reads_persisted_state(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    cli_obj = _make_cli()
    state_path = tmp_path / "goal_123.json"
    save_goal_state(
        GoalRunState(
            run_id="goal_123",
            session_id="sess-123",
            contract=GoalContract(goal="finish oauth", done_when=["DONE"]),
            status="approval_required",
            attempts_used=2,
            next_action="await_approval",
            stop_requested=False,
            last_attempt_summary="waiting for approval",
        ),
        state_path,
    )
    cli_obj._goal_runs = {
        "goal_123": {
            "goal": "finish oauth",
            "state": "running",
            "state_path": str(state_path),
            "thread": None,
            "last_summary": "",
        }
    }

    with patch("cli._cprint") as mock_cprint:
        cli_obj._handle_goal_status_command("/goal-status goal_123")

    printed = "\n".join(call.args[0] for call in mock_cprint.call_args_list)
    assert "State: approval_required" in printed
    assert "Attempts used: 2" in printed
    assert "Next action: await_approval" in printed
    assert "Stop requested: no" in printed


def test_goal_stop_persists_stop_requested(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    cli_obj = _make_cli()
    state_path = tmp_path / "goal_456.json"
    save_goal_state(
        GoalRunState(
            run_id="goal_456",
            session_id="sess-123",
            contract=GoalContract(goal="finish oauth"),
            status="approval_required",
            next_action="await_approval",
        ),
        state_path,
    )
    cli_obj._goal_runs = {
        "goal_456": {
            "goal": "finish oauth",
            "state": "approval_required",
            "state_path": str(state_path),
            "thread": None,
            "last_summary": "",
        }
    }

    with patch("cli._cprint"):
        cli_obj._handle_goal_stop_command("/goal-stop goal_456")

    persisted = Path(state_path)
    assert persisted.exists()
    from agent.goal_until_done import load_goal_state
    state = load_goal_state(state_path)
    assert state.stop_requested is True
    assert state.next_action == "stop_requested_by_user"



def test_goal_stop_interrupts_active_attempt(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    cli_obj = _make_cli()
    state_path = tmp_path / "goal_active.json"
    save_goal_state(
        GoalRunState(
            run_id="goal_active",
            session_id="sess-123",
            contract=GoalContract(goal="finish oauth"),
            status="running",
        ),
        state_path,
    )
    active_agent = MagicMock()
    cli_obj._goal_runs = {
        "goal_active": {
            "goal": "finish oauth",
            "state": "running",
            "state_path": str(state_path),
            "thread": MagicMock(),
            "agent": active_agent,
            "last_summary": "",
        }
    }

    with patch("cli._cprint"):
        cli_obj._handle_goal_stop_command("/goal-stop goal_active")

    active_agent.interrupt.assert_called_once_with()


def test_goal_resume_clears_stop_requested_and_restarts(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    cli_obj = _make_cli()
    cli_obj.max_turns = 90
    cli_obj.enabled_toolsets = []
    cli_obj.reasoning_config = None
    cli_obj.service_tier = None
    cli_obj._providers_only = None
    cli_obj._providers_ignore = None
    cli_obj._providers_order = None
    cli_obj._provider_sort = None
    cli_obj._provider_require_params = False
    cli_obj._provider_data_collection = None
    cli_obj._fallback_model = None
    cli_obj._session_db = MagicMock()
    cli_obj._ensure_runtime_credentials = MagicMock(return_value=True)
    cli_obj._resolve_turn_agent_config = MagicMock(return_value={
        "model": "gpt-5.4",
        "runtime": {"api_key": "***", "base_url": "", "provider": "openai", "api_mode": None, "command": None, "args": None},
        "request_overrides": None,
    })
    cli_obj._invalidate = MagicMock()

    state_path = tmp_path / "goal_789.json"
    save_goal_state(
        GoalRunState(
            run_id="goal_789",
            session_id="sess-123",
            contract=GoalContract(goal="finish oauth"),
            status="stopped",
            attempts_used=1,
            next_action="stopped_by_user",
            stop_requested=True,
        ),
        state_path,
    )
    cli_obj._goal_runs = {
        "goal_789": {
            "goal": "finish oauth",
            "state": "stopped",
            "state_path": str(state_path),
            "thread": None,
            "last_summary": "",
        }
    }

    fake_thread = MagicMock()
    fake_thread.start = MagicMock()

    with patch("cli.AIAgent") as mock_agent_cls, \
         patch("cli.threading.Thread", return_value=fake_thread), \
         patch("cli._cprint"):
        cli_obj._handle_goal_resume_command("/goal-resume goal_789")

    from agent.goal_until_done import load_goal_state
    state = load_goal_state(state_path)
    assert state.stop_requested is False
    assert state.status == "running"
    fake_thread.start.assert_called_once()
    mock_agent_cls.assert_not_called()


def test_goal_run_prints_approval_guidance(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    cli_obj = _make_cli()
    cli_obj.max_turns = 90
    cli_obj.enabled_toolsets = []
    cli_obj.reasoning_config = None
    cli_obj.service_tier = None
    cli_obj._providers_only = None
    cli_obj._providers_ignore = None
    cli_obj._providers_order = None
    cli_obj._provider_sort = None
    cli_obj._provider_require_params = False
    cli_obj._provider_data_collection = None
    cli_obj._fallback_model = None
    cli_obj._session_db = MagicMock()
    cli_obj._app = None

    task_id = "goal_approval"
    state_path = tmp_path / f"{task_id}.json"
    save_goal_state(
        GoalRunState(
            run_id=task_id,
            session_id=task_id,
            contract=GoalContract(goal="finish oauth"),
            status="approval_required",
            next_action="await_approval",
            last_attempt_summary="need approval",
        ),
        state_path,
    )

    turn_route = {
        "model": "gpt-5.4",
        "runtime": {"api_key": "***", "base_url": "", "provider": "openai", "api_mode": None, "command": None, "args": None},
        "request_overrides": None,
    }

    fake_thread = None

    def run_target_immediately(*args, **kwargs):
        nonlocal fake_thread
        target = kwargs.get("target")
        fake_thread = MagicMock()
        fake_thread.start = lambda: target()
        return fake_thread

    with patch("cli.AIAgent") as mock_agent_cls, \
         patch("cli.threading.Thread", side_effect=run_target_immediately), \
         patch("cli._cprint") as mock_cprint, \
         patch("cli.ChatConsole.print"):
        mock_agent = MagicMock()
        mock_agent.run_until_done = MagicMock()
        mock_agent_cls.return_value = mock_agent
        cli_obj._start_goal_run(task_id, "finish oauth", GoalContract(goal="finish oauth"), state_path, turn_route)

    printed = "\n".join(call.args[0] for call in mock_cprint.call_args_list)
    assert f"finished with status: approval_required" in printed
    assert "/goal-resume" in printed
    assert "/goal-stop" in printed
