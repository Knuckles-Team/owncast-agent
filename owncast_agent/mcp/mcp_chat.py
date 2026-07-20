"""MCP tools for chat operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from agent_utilities.mcp.action_dispatch import resolve_action
from agent_utilities.mcp.concurrency import run_blocking
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from owncast_agent.auth import get_client
from owncast_agent.mcp_server import ALLOWED_CHAT_ACTIONS


def register_chat_tools(mcp: FastMCP):
    """Register consolidated action-routed tools for chat operations.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """

    @mcp.tool(tags={"chat"})
    async def owncast_chat(
        action: str = Field(
            description="Action to perform. Must be one of: "
            + ", ".join(sorted(f"'{a}'" for a in ALLOWED_CHAT_ACTIONS))
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage owncast chat operations.

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        resolved = resolve_action(action, ALLOWED_CHAT_ACTIONS, service="owncast-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved

        method = getattr(client, action)
        return await run_blocking(method, **kwargs)
