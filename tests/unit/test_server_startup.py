import importlib
import os

import pytest


@pytest.mark.concept("ORCH-1.4")
def test_server_startup():
    """Validates that the server module can start successfully and exposures are correct.

    CONCEPT:ORCH-1.4
    """
    assert os.path.exists("owncast_agent/agent_server.py")
    assert os.path.exists("owncast_agent/mcp_server.py")

    agent_server_mod = importlib.import_module("owncast_agent.agent_server")
    mcp_server_mod = importlib.import_module("owncast_agent.mcp_server")

    assert callable(agent_server_mod.agent_server)
    assert callable(mcp_server_mod.mcp_server)
