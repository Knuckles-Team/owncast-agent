import importlib
import os

import pytest


@pytest.mark.concept("AU-ORCH.adapter.kg-graph-materialization")
def test_server_startup():
    """Validates that the server module can start successfully and exposures are correct.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    # agent_server.py (the standalone pydantic-ai A2A runtime) was retired
    # (SDK-GAPS.md #11); only mcp_server.py is still a live entry point.
    assert os.path.exists("owncast_agent/mcp_server.py")

    mcp_server_mod = importlib.import_module("owncast_agent.mcp_server")

    assert callable(mcp_server_mod.mcp_server)
