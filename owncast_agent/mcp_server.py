import os
import sys
import logging
from typing import Any, Dict
from dotenv import load_dotenv, find_dotenv
from fastmcp import FastMCP

__version__ = "0.1.3"

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from .auth import get_client

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def register_status_tools(mcp: FastMCP):
    @mcp.tool(
        name="owncast-get-status", description="Get the current Owncast stream status"
    )
    def owncast_get_status() -> Dict[str, Any]:
        return get_client().get_status()

    @mcp.tool(
        name="owncast-get-config", description="Get the server configuration details"
    )
    def owncast_get_config() -> Dict[str, Any]:
        return get_client().get_config()


def register_chat_tools(mcp: FastMCP):
    @mcp.tool(
        name="owncast-send-chat-message", description="Send a standard chat message"
    )
    def owncast_send_chat_message(author: str, body: str) -> Dict[str, Any]:
        return get_client().send_chat_message(author, body)

    @mcp.tool(
        name="owncast-send-system-message",
        description="Send a system message (no author)",
    )
    def owncast_send_system_message(body: str) -> Dict[str, Any]:
        return get_client().send_system_message(body)

    @mcp.tool(
        name="owncast-send-action-message",
        description="Send an action message (e.g., author dances)",
    )
    def owncast_send_action_message(author: str, body: str) -> Dict[str, Any]:
        return get_client().send_action_message(author, body)

    @mcp.tool(name="owncast-get-chat", description="Get the recent chat history")
    def owncast_get_chat() -> Dict[str, Any]:
        return get_client().get_chat_history()


def register_prompts(mcp: FastMCP):
    @mcp.prompt(
        name="owncast-system-summary",
        description="Get a summary of the Owncast server status",
    )
    def owncast_system_summary() -> str:
        return "Check the current stream status, viewer count, and active configuration for the Owncast instance."


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    load_dotenv(find_dotenv())

    args, mcp, middlewares = create_mcp_server(
        name="owncast",
        version=__version__,
        instructions="Owncast Agent MCP Server",
    )

    registered_tags = []

    if to_boolean(os.getenv("STATUSTOOL", "True")):
        register_status_tools(mcp)
        registered_tags.append("status")

    if to_boolean(os.getenv("CHATTOOL", "True")):
        register_chat_tools(mcp)
        registered_tags.append("chat")

    register_prompts(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)

    return mcp, args, middlewares, registered_tags


def mcp_server():
    mcp, args, middlewares, registered_tags = get_mcp_instance()

    print(f"Owncast Agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)
    print(f"  Dynamic Tags Loaded: {registered_tags}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error(f"Invalid transport: {args.transport}")
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
