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
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from starlette.requests import Request
from starlette.responses import JSONResponse

from owncast_agent.auth import get_client

__version__ = "0.31.0"

logger = get_logger(name="owncast-agent")
logger.setLevel(logging.INFO)

ALLOWED_INTERNAL_ACTIONS = {
    "get_status",
    "get_custom_emoji_list",
    "get_chat_messages",
    "register_anonymous_chat_user",
    "update_message_visibility",
    "update_user_enabled",
    "get_web_config",
    "get_ypresponse",
    "get_all_social_platforms",
    "get_video_stream_output_variants",
    "ping",
    "remote_follow",
    "get_followers",
    "report_playback_metrics",
    "register_for_live_notifications",
    "status_admin",
    "disconnect_inbound_connection",
    "get_server_config",
    "get_viewers_over_time",
    "get_active_viewers",
    "get_hardware_stats",
    "get_connected_chat_clients",
    "get_chat_messages_admin",
    "update_message_visibility_admin",
    "update_user_enabled_admin",
    "get_disabled_users",
    "ban_ipaddress",
    "unban_ipaddress",
    "get_ipaddress_bans",
    "update_user_moderator",
    "get_moderators",
    "get_logs",
    "get_warnings",
    "get_followers_admin",
    "get_pending_follow_requests",
    "get_blocked_and_rejected_followers",
    "approve_follower",
    "upload_custom_emoji",
    "delete_custom_emoji",
    "set_admin_password",
    "set_stream_keys",
    "set_extra_page_content",
    "set_stream_title",
    "set_server_welcome_message",
    "set_chat_disabled",
    "set_chat_join_messages_enabled",
    "set_enable_established_chat_user_mode",
    "set_forbidden_username_list",
    "set_suggested_username_list",
    "set_chat_spam_protection_enabled",
    "set_chat_slur_filter_enabled",
    "set_chat_require_authentication",
    "set_video_codec",
    "set_stream_latency_level",
    "set_stream_output_variants",
    "set_custom_color_variable_values",
    "set_logo",
    "set_favicon",
    "reset_favicon",
    "set_tags",
    "set_ffmpeg_path",
    "set_web_server_port",
    "set_web_server_ip",
    "set_rtmpserver_port",
    "set_socket_host_override",
    "set_video_serving_endpoint",
    "set_nsfw",
    "set_directory_enabled",
    "set_social_handles",
    "set_s3_configuration",
    "set_server_url",
    "set_external_actions",
    "set_custom_styles",
    "set_custom_javascript",
    "set_hide_viewer_count",
    "set_disable_search_indexing",
    "set_federation_enabled",
    "set_federation_activity_private",
    "set_federation_show_engagement",
    "set_federation_username",
    "set_federation_go_live_message",
    "set_federation_block_domains",
    "set_discord_notification_configuration",
    "set_browser_notification_configuration",
    "get_webhooks",
    "delete_webhook",
    "create_webhook",
    "get_external_apiusers",
    "delete_external_apiuser",
    "create_external_apiuser",
    "auto_update_options",
    "auto_update_start",
    "auto_update_force_quit",
    "reset_ypregistration",
    "get_video_playback_metrics",
    "get_prometheus_api",
    "post_prometheus_api",
    "put_prometheus_api",
    "delete_prometheus_api",
    "send_federated_message",
    "get_federated_actions",
    "start_indie_auth_flow",
    "handle_indie_auth_redirect",
    "handle_indie_auth_endpoint_get",
    "handle_indie_auth_endpoint_post",
    "register_fediverse_otprequest",
    "verify_fediverse_otprequest",
}

ALLOWED_OBJECTS_ACTIONS = {
    "set_server_name",
    "set_server_summary",
    "set_custom_offline_message",
}

ALLOWED_EXTERNAL_ACTIONS = {
    "send_system_message",
    "send_system_message_to_connected_client",
    "send_user_message",
    "send_integration_chat_message",
    "send_chat_action",
    "external_update_message_visibility",
    "external_get_status",
    "external_set_stream_title",
    "external_get_chat_messages",
    "external_get_connected_chat_clients",
    "external_get_user_details",
}

ALLOWED_CHAT_ACTIONS = {"get_user_details"}


def register_internal_tools(mcp: FastMCP):
    """Register consolidated action-routed tools for internal operations."""

    @mcp.tool(tags={"internal"})
    async def owncast_internal(
        action: str = Field(
            description="Action to perform. Must be one of: "
            + ", ".join(sorted(f"'{a}'" for a in ALLOWED_INTERNAL_ACTIONS))
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage owncast internal operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action not in ALLOWED_INTERNAL_ACTIONS:
            raise ValueError(f"Unknown action: {action}")

        method = getattr(client, action)
        return method(**kwargs)


def register_objects_tools(mcp: FastMCP):
    """Register consolidated action-routed tools for objects operations."""

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
        """Manage owncast objects operations."""
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


def register_external_tools(mcp: FastMCP):
    """Register consolidated action-routed tools for external operations."""

    @mcp.tool(tags={"external"})
    async def owncast_external(
        action: str = Field(
            description="Action to perform. Must be one of: "
            + ", ".join(sorted(f"'{a}'" for a in ALLOWED_EXTERNAL_ACTIONS))
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage owncast external operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action not in ALLOWED_EXTERNAL_ACTIONS:
            raise ValueError(f"Unknown action: {action}")

        method = getattr(client, action)
        return method(**kwargs)


def register_chat_tools(mcp: FastMCP):
    """Register consolidated action-routed tools for chat operations."""

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
        """Manage owncast chat operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action not in ALLOWED_CHAT_ACTIONS:
            raise ValueError(f"Unknown action: {action}")

        method = getattr(client, action)
        return method(**kwargs)


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="owncast-agent MCP",
        version=__version__,
        instructions="owncast-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    DEFAULT_INTERNALTOOL = to_boolean(os.getenv("INTERNALTOOL", "True"))
    if DEFAULT_INTERNALTOOL:
        register_internal_tools(mcp)
    DEFAULT_OBJECTSTOOL = to_boolean(os.getenv("OBJECTSTOOL", "True"))
    if DEFAULT_OBJECTSTOOL:
        register_objects_tools(mcp)
    DEFAULT_EXTERNALTOOL = to_boolean(os.getenv("EXTERNALTOOL", "True"))
    if DEFAULT_EXTERNALTOOL:
        register_external_tools(mcp)
    DEFAULT_CHATTOOL = to_boolean(os.getenv("CHATTOOL", "True"))
    if DEFAULT_CHATTOOL:
        register_chat_tools(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    """Run the MCP server."""
    mcp, args, middlewares = get_mcp_instance()
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
