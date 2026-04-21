from agent.goal_until_done import GoalContract, load_goal_state, run_until_done, save_goal_state


def test_run_until_done_retries_then_completes(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    calls = []

    def callback(attempt_index, attempt_prompt):
        calls.append((attempt_index, attempt_prompt))
        if attempt_index == 1:
            raise RuntimeError("temporary")
        return {"final_response": "DONE tests pass", "completed": True}

    contract = GoalContract(
        goal="finish",
        done_when=["done"],
        retry_policy={"max_attempts": 3, "backoff_seconds": [0]},
    )
    state = run_until_done(contract, callback, session_id="sess", sleep_fn=lambda _: None)

    assert state.status == "completed"
    assert state.attempts_used == 2
    assert len(calls) == 2
    assert "[GOAL] finish" in calls[0][1]


def test_run_until_done_pauses_on_approval_required(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))

    def callback(attempt_index, attempt_prompt):
        return {"final_response": "blocked", "tool_failures": ["permission denied"]}

    contract = GoalContract(goal="finish")
    state = run_until_done(contract, callback, session_id="sess", sleep_fn=lambda _: None)

    assert state.status == "approval_required"
    assert state.next_action == "await_approval"


def test_run_until_done_stops_after_stop_requested(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    calls = []
    state_path = tmp_path / "goal-state.json"

    def callback(attempt_index, attempt_prompt):
        calls.append((attempt_index, attempt_prompt))
        state = load_goal_state(state_path)
        state.stop_requested = True
        save_goal_state(state, state_path)
        return {"final_response": "still working"}

    contract = GoalContract(goal="finish", retry_policy={"max_attempts": 3, "backoff_seconds": [0]})
    state = run_until_done(
        contract,
        callback,
        session_id="sess",
        state_path=state_path,
        sleep_fn=lambda _: None,
    )

    assert state.status == "stopped"
    assert state.next_action == "stopped_by_user"
    assert state.stop_requested is True
    assert state.attempts_used == 1
    assert len(calls) == 1
