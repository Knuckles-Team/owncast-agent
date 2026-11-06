#!/usr/bin/python
import warnings

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import sys
from typing import Any

from scion_sdk.config import load_config
from scion_sdk.connector import build_server
from scion_sdk.connector_identity import connector_version
from scion_sdk.mcp.tool_surface import register_tool_surface
from starlette.requests import Request
from starlette.responses import JSONResponse

from owncast_agent.api_client import OwncastApi
from owncast_agent.auth import get_client

__version__ = connector_version("owncast_agent")

logger = get_logger(name="owncast-agent")
logger.setLevel(logging.INFO)


def register_kg_tools(mcp: FastMCP):
    """Register the Wire-First native KG ingestion tool.

    Lists live Owncast telemetry through the real client and pushes it into the ONE
    medulla knowledge graph as typed :Stream / :Viewer / :ViewerSample /
    :HardwareSample / :ChatMessage / :Person nodes. Best-effort + engine-guarded:
    returns ``{"ingested": None}`` when no engine is reachable.
    CONCEPT:AU-KG.ingest.enterprise-source-extractor.
    """

    @mcp.tool(tags={"kg"})
    async def owncast_ingest_telemetry(
        include: str = Field(
            default="status,viewers,viewers_over_time,hardware,followers,chat",
            description=(
                "Comma-separated modalities to ingest: any of "
                "status, viewers, viewers_over_time, hardware, followers, chat."
            ),
        ),
        access_token: str | None = Field(
            default=None,
            description="Access token for chat message retrieval (chat modality only).",
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Ingest live Owncast telemetry into medulla as typed nodes + timeseries."""
        if ctx:
            await ctx.info("Ingesting Owncast telemetry into the knowledge graph...")

        from owncast_agent import kg_ingest

        instance = getattr(client, "base_url", None)
        wanted = {w.strip() for w in include.split(",") if w.strip()}
        return await kg_ingest.ingest_selected_telemetry(
            client, wanted, access_token=access_token, instance=instance
        )


def register_server_surface(mcp: FastMCP) -> list[str]:
    """Reuse the existing health route and tool registrars in legacy order."""

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    registered_tags = register_tool_surface(
        mcp,
        client_cls=OwncastApi,
        get_client=get_client,
        service="owncast-agent",
        tools_module=sys.modules[__name__],
    )

    return registered_tags


def get_mcp_instance(*, command_args=None) -> tuple[Any, ...]:
    """Preserve legacy configuration and the four-item startup tuple."""
    load_config()
    args, mcp = build_server("owncast_agent", command_args=command_args)
    return mcp, args, list(mcp.middleware), mcp._owncast_registered_tags


def mcp_server() -> None:
    """Run the MCP server."""
    mcp, args, middlewares, *_ = get_mcp_instance()
    print(f"owncast-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
