from unittest.mock import MagicMock, patch

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
    assert resolve_command("ud").name == "until-done"


def test_process_command_dispatches_until_done():
    cli_obj = _make_cli()
    with patch.object(cli_obj, "_handle_until_done_command") as mock_handler:
        assert cli_obj.process_command("/until-done finish oauth") is True
    mock_handler.assert_called_once_with("/until-done finish oauth")


def test_process_command_dispatches_goal_status_and_stop():
    cli_obj = _make_cli()
    with patch.object(cli_obj, "_handle_goal_status_command") as mock_status, \
         patch.object(cli_obj, "_handle_goal_stop_command") as mock_stop:
        assert cli_obj.process_command("/goal-status") is True
        assert cli_obj.process_command("/goal-stop") is True
    mock_status.assert_called_once_with("/goal-status")
    mock_stop.assert_called_once_with("/goal-stop")
