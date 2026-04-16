from pathlib import Path

from agent.goal_until_done import GoalContract, GoalRunState, save_goal_state, load_goal_state


def test_goal_state_roundtrip(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    contract = GoalContract(goal="finish task", done_when=["DONE"])
    state = GoalRunState(run_id="run1", session_id="sess1", contract=contract, status="running")

    saved = save_goal_state(state)
    loaded = load_goal_state(saved)

    assert loaded.run_id == "run1"
    assert loaded.session_id == "sess1"
    assert loaded.contract.goal == "finish task"
    assert loaded.contract.done_when == ["DONE"]
    assert Path(saved).exists()
