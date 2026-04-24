"""Regression tests for approval-state cleanup on session boundaries."""

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from gateway.config import Platform
from gateway.platforms.base import MessageEvent
from gateway.session import SessionEntry, SessionSource, build_session_key
from tools import approval as approval_mod
from tools.approval import (
    approve_session,
    enable_session_yolo,
    is_approved,
    is_session_yolo_enabled,
)


@pytest.fixture(autouse=True)
def _clear_approval_state():
    approval_mod._gateway_queues.clear()
    approval_mod._gateway_notify_cbs.clear()
    approval_mod._session_approved.clear()
    approval_mod._session_yolo.clear()
    approval_mod._permanent_approved.clear()
    approval_mod._pending.clear()
    yield
    approval_mod._gateway_queues.clear()
    approval_mod._gateway_notify_cbs.clear()
    approval_mod._session_approved.clear()
    approval_mod._session_yolo.clear()
    approval_mod._permanent_approved.clear()
    approval_mod._pending.clear()


def _make_source() -> SessionSource:
    return SessionSource(
        platform=Platform.TELEGRAM,
        user_id="u1",
        chat_id="c1",
        user_name="tester",
        chat_type="dm",
    )


def _make_event(text: str) -> MessageEvent:
    return MessageEvent(text=text, source=_make_source(), message_id="m1")


def _make_entry(session_id: str, source: SessionSource | None = None) -> SessionEntry:
    source = source or _make_source()
    return SessionEntry(
        session_key=build_session_key(source),
        session_id=session_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        origin=source,
        platform=source.platform,
        chat_type=source.chat_type,
    )


def _make_resume_runner():
    from gateway.run import GatewayRunner

    source = _make_source()
    session_key = build_session_key(source)
    current_entry = _make_entry("current-session", source)
    resumed_entry = _make_entry("resumed-session", source)

    runner = object.__new__(GatewayRunner)
    runner.adapters = {}
    runner._background_tasks = set()
    runner._async_flush_memories = AsyncMock()
    runner._running_agents = {}
    runner._running_agents_ts = {}
    runner._busy_ack_ts = {}
    runner._pending_approvals = {}
    runner._agent_cache = {}
    runner._agent_cache_lock = None
    runner.session_store = MagicMock()
    runner.session_store.get_or_create_session.return_value = current_entry
    runner.session_store.switch_session.return_value = resumed_entry
    runner.session_store.load_transcript.return_value = []
    runner._session_db = MagicMock()
    runner._session_db.resolve_session_by_title.return_value = "resumed-session"
    runner._session_db.get_session_title.return_value = "Resumed Work"
    return runner, session_key


def _make_branch_runner():
    from gateway.run import GatewayRunner

    source = _make_source()
    session_key = build_session_key(source)
    current_entry = _make_entry("current-session", source)
    branched_entry = _make_entry("branch-session", source)

    runner = object.__new__(GatewayRunner)
    runner.adapters = {}
    runner._background_tasks = set()
    runner._running_agents = {}
    runner._running_agents_ts = {}
    runner._busy_ack_ts = {}
    runner._pending_approvals = {}
    runner._agent_cache = {}
    runner._agent_cache_lock = None
    runner._session_db = MagicMock()
    runner._session_db.set_session_title = MagicMock()
    runner._session_db.resolve_session_by_title.return_value = None
    runner.config = {}
    runner.session_store = MagicMock()
    runner.session_store.get_or_create_session.return_value = current_entry
    runner.session_store.load_transcript.return_value = [{"role": "user", "content": "hello"}]
    runner.session_store.switch_session.return_value = branched_entry
    runner._evict_cached_agent = MagicMock()
    return runner, session_key


@pytest.mark.asyncio
async def test_resume_clears_session_scoped_approval_and_yolo_state():
    runner, session_key = _make_resume_runner()
    other_key = "agent:main:telegram:dm:other-chat"

    approve_session(session_key, "recursive delete")
    approve_session(other_key, "recursive delete")
    enable_session_yolo(session_key)
    enable_session_yolo(other_key)
    runner._pending_approvals[session_key] = {"command": "rm -rf /tmp/demo"}
    runner._pending_approvals[other_key] = {"command": "rm -rf /tmp/other"}

    result = await runner._handle_resume_command(_make_event("/resume Resumed Work"))

    assert "Resumed session" in result
    assert is_approved(session_key, "recursive delete") is False
    assert is_session_yolo_enabled(session_key) is False
    assert session_key not in runner._pending_approvals
    assert is_approved(other_key, "recursive delete") is True
    assert is_session_yolo_enabled(other_key) is True
    assert other_key in runner._pending_approvals


@pytest.mark.asyncio
async def test_branch_clears_session_scoped_approval_and_yolo_state():
    runner, session_key = _make_branch_runner()
    other_key = "agent:main:telegram:dm:other-chat"

    approve_session(session_key, "recursive delete")
    approve_session(other_key, "recursive delete")
    enable_session_yolo(session_key)
    enable_session_yolo(other_key)
    runner._pending_approvals[session_key] = {"command": "rm -rf /tmp/demo"}
    runner._pending_approvals[other_key] = {"command": "rm -rf /tmp/other"}

    result = await runner._handle_branch_command(_make_event("/branch"))

    assert "Branched to" in result
    assert is_approved(session_key, "recursive delete") is False
    assert is_session_yolo_enabled(session_key) is False
    assert session_key not in runner._pending_approvals
    assert is_approved(other_key, "recursive delete") is True
    assert is_session_yolo_enabled(other_key) is True
    assert other_key in runner._pending_approvals


def test_clear_session_boundary_security_state_is_scoped():
    """The helper must wipe only the target session's approval/yolo state."""
    from gateway.run import GatewayRunner

    runner = object.__new__(GatewayRunner)
    runner._pending_approvals = {}

    source = _make_source()
    session_key = build_session_key(source)
    other_key = "agent:main:telegram:dm:other-chat"

    approve_session(session_key, "recursive delete")
    approve_session(other_key, "recursive delete")
    enable_session_yolo(session_key)
    enable_session_yolo(other_key)
    runner._pending_approvals[session_key] = {"command": "rm -rf /tmp/demo"}
    runner._pending_approvals[other_key] = {"command": "rm -rf /tmp/other"}

    runner._clear_session_boundary_security_state(session_key)

    assert is_approved(session_key, "recursive delete") is False
    assert is_session_yolo_enabled(session_key) is False
    assert session_key not in runner._pending_approvals
    assert is_approved(other_key, "recursive delete") is True
    assert is_session_yolo_enabled(other_key) is True
    assert other_key in runner._pending_approvals

    runner._clear_session_boundary_security_state("")
    assert is_approved(other_key, "recursive delete") is True


@pytest.mark.asyncio
async def test_reset_clears_session_scoped_approval_and_yolo_state():
    from gateway.run import GatewayRunner

    source = _make_source()
    session_key = build_session_key(source)
    old_entry = _make_entry("current-session", source)
    new_entry = _make_entry("new-session", source)
    other_key = "agent:main:telegram:dm:other-chat"

    runner = object.__new__(GatewayRunner)
    runner.adapters = {}
    runner._background_tasks = set()
    runner._async_flush_memories = AsyncMock()
    runner._running_agents = {}
    runner._running_agents_ts = {}
    runner._busy_ack_ts = {}
    runner._pending_approvals = {}
    runner._agent_cache = {}
    runner._agent_cache_lock = None
    runner._session_model_overrides = {}
    runner._cleanup_agent_resources = MagicMock()
    runner._evict_cached_agent = MagicMock()
    runner._format_session_info = MagicMock(return_value="")
    runner.hooks = MagicMock()
    runner.hooks.emit = AsyncMock()
    runner.session_store = MagicMock()
    runner.session_store._entries = {session_key: old_entry}
    runner.session_store.reset_session.return_value = new_entry
    runner.session_store.get_or_create_session.return_value = old_entry
    runner._session_key_for_source = MagicMock(return_value=session_key)

    approve_session(session_key, "recursive delete")
    approve_session(other_key, "recursive delete")
    enable_session_yolo(session_key)
    enable_session_yolo(other_key)
    runner._pending_approvals[session_key] = {"command": "rm -rf /tmp/demo"}
    runner._pending_approvals[other_key] = {"command": "rm -rf /tmp/other"}

    result = await runner._handle_reset_command(_make_event("/new"))

    assert "Session reset" in result or "New session started" in result
    assert is_approved(session_key, "recursive delete") is False
    assert is_session_yolo_enabled(session_key) is False
    assert session_key not in runner._pending_approvals
    assert is_approved(other_key, "recursive delete") is True
    assert is_session_yolo_enabled(other_key) is True
    assert other_key in runner._pending_approvals
