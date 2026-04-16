from agent.goal_until_done import GoalContract, classify_attempt_outcome


def test_classifier_completed_on_done_when_match():
    contract = GoalContract(goal="ship", done_when=["tests pass", "qa complete"])
    result = {"final_response": "All done: tests pass and qa complete."}
    assert classify_attempt_outcome(contract, result) == "completed"


def test_classifier_retryable_on_exception():
    contract = GoalContract(goal="ship")
    assert classify_attempt_outcome(contract, exception=RuntimeError("network")) == "retryable_failure"


def test_classifier_approval_required_on_tool_failure_text():
    contract = GoalContract(goal="ship")
    assert classify_attempt_outcome(contract, tool_failures=["Permission denied for Bash"]) == "approval_required"


def test_classifier_retryable_when_not_done_and_no_terminal_signal():
    contract = GoalContract(goal="ship", done_when=["done"])
    result = {"final_response": "still working"}
    assert classify_attempt_outcome(contract, result) == "retryable_failure"
