from pathlib import Path

from agent.goal_until_done import GoalContract
from run_agent import AIAgent


class DummyAgent(AIAgent):
    def __init__(self):
        self.session_id = "sess-123"
        self.calls = []

    def run_conversation(self, user_message, system_message=None, conversation_history=None, task_id=None, stream_callback=None, persist_user_message=None):
        self.calls.append(user_message)
        if len(self.calls) == 1:
            return {"final_response": "not yet"}
        return {"final_response": "DONE tests pass", "completed": True}

    def get_activity_summary(self):
        return {"budget_used": len(self.calls), "idle_seconds": 0.0}


def test_aiagent_run_until_done_uses_repeated_attempts(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".hermes"))
    agent = DummyAgent()
    contract = GoalContract(goal="ship", done_when=["done"], retry_policy={"max_attempts": 3, "backoff_seconds": [0]})
    state = agent.run_until_done(contract, state_path=tmp_path / "state.json")

    assert state.status == "completed"
    assert len(agent.calls) == 2
    assert Path(tmp_path / "state.json").exists()
    assert "[DONE WHEN]" in agent.calls[0]
