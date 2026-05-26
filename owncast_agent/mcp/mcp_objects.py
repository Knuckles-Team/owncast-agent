"""MCP tools for objects operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from owncast_agent.auth import get_client
from owncast_agent.mcp_server import ALLOWED_OBJECTS_ACTIONS


def register_objects_tools(mcp: FastMCP):
    """Register consolidated action-routed tools for objects operations.

    CONCEPT:ECO-4.1
    """

    @mcp.tool(tags={"objects"})
    async def owncast_objects(
        action: str = Field(
            description="Action to perform. Must be one of: "
            + ", ".join(sorted(f"'{a}'" for a in ALLOWED_OBJECTS_ACTIONS))
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage owncast objects operations.

        CONCEPT:ECO-4.1
        """
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action not in ALLOWED_OBJECTS_ACTIONS:
            raise ValueError(f"Unknown action: {action}")

        method = getattr(client, action)
        return method(**kwargs)
