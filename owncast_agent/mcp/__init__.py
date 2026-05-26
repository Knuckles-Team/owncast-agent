"""MCP tool registration modules for owncast-agent.

Auto-generated during ecosystem standardization.
Each domain has its own module with a register_*_tools function.
"""

from owncast_agent.mcp.mcp_chat import register_chat_tools
from owncast_agent.mcp.mcp_external import register_external_tools
from owncast_agent.mcp.mcp_internal import register_internal_tools
from owncast_agent.mcp.mcp_objects import register_objects_tools

__all__ = [
    "register_chat_tools",
    "register_external_tools",
    "register_internal_tools",
    "register_objects_tools",
]
