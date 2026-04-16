from agent.goal_until_done import GoalContract, run_until_done


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
