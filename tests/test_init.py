from fastmcp import FastMCP

from owncast_agent.mcp_server import get_mcp_instance


def test_mcp_instance_creation():
    """Test that the MCP instance can be created successfully."""
    # We might need to mock some env vars if the implementation requires them
    mcp, args, middlewares, registered_tags = get_mcp_instance()
    assert isinstance(mcp, FastMCP)
    assert "owncast" in mcp.name

def test_import_owncast_agent():
    """Test that the package can be imported."""
    pass
