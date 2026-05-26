import pytest

from owncast_agent.owncast_models import (
    ActionMessage,
    ChatMessage,
    OwncastStatusResponse,
    SystemMessage,
)


@pytest.mark.concept("ECO-4.1")
def test_models():
    """Verify that all Pydantic models can be instantiated and validated with correct types.

    CONCEPT:ECO-4.1
    """
    status = OwncastStatusResponse(
        online=True,
        viewerCount=10,
        overallMaxViewerCount=100,
        sessionMaxViewerCount=50,
        lastConnectTime="2026-05-22T00:00:00Z",
        lastDisconnectTime=None,
        streamTitle="Test Stream",
    )
    assert status.online is True
    assert status.viewerCount == 10
    assert status.overallMaxViewerCount == 100
    assert status.sessionMaxViewerCount == 50
    assert status.lastConnectTime == "2026-05-22T00:00:00Z"
    assert status.lastDisconnectTime is None
    assert status.streamTitle == "Test Stream"

    chat = ChatMessage(author="alice", body="hello")
    assert chat.author == "alice"
    assert chat.body == "hello"

    system = SystemMessage(body="system broadcast")
    assert system.body == "system broadcast"

    action = ActionMessage(author="bob", body="waved")
    assert action.author == "bob"
    assert action.body == "waved"
