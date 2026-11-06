"""CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R002: one typed tool per operation, no action router."""

from __future__ import annotations

import importlib
import os
from unittest.mock import patch

import pytest
from scion_sdk.mcp.tool_surface import registered_tools

pytestmark = pytest.mark.spec("CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R002")

ROUTERS = {"owncast_internal", "owncast_objects", "owncast_external", "owncast_chat"}


def test_every_tool_is_typed_and_no_router_is_served() -> None:
    module = importlib.import_module("owncast_agent.mcp_server")
    env = {"OWNCAST_URL": "http://owncast.invalid", "OWNCAST_ACCESS_TOKEN": "x"}
    with (
        patch.dict(os.environ, env),
        patch("sys.argv", ["c", "--transport", "stdio", "--auth-type", "none"]),
    ):
        mcp = module.get_mcp_instance()[0]
    tools = registered_tools(mcp)
    assert len(tools) > 100
    assert not ROUTERS & set(tools)
    for name, tool in tools.items():
        props = tool.parameters.get("properties", {})
        assert "action" not in props, name
        assert "params_json" not in props, name
