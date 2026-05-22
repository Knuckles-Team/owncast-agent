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

__version__ = "0.12.0"

logger = get_logger(name="owncast-agent")
logger.setLevel(logging.INFO)


def register_internal_tools(mcp: FastMCP):
    @mcp.tool(tags={"internal"})
    async def owncast_internal(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_status', 'get_custom_emoji_list', 'get_chat_messages', 'register_anonymous_chat_user', 'update_message_visibility', 'update_user_enabled', 'get_web_config', 'get_ypresponse', 'get_all_social_platforms', 'get_video_stream_output_variants', 'ping', 'remote_follow', 'get_followers', 'report_playback_metrics', 'register_for_live_notifications', 'status_admin', 'disconnect_inbound_connection', 'get_server_config', 'get_viewers_over_time', 'get_active_viewers', 'get_hardware_stats', 'get_connected_chat_clients', 'get_chat_messages_admin', 'update_message_visibility_admin', 'update_user_enabled_admin', 'get_disabled_users', 'ban_ipaddress', 'unban_ipaddress', 'get_ipaddress_bans', 'update_user_moderator', 'get_moderators', 'get_logs', 'get_warnings', 'get_followers_admin', 'get_pending_follow_requests', 'get_blocked_and_rejected_followers', 'approve_follower', 'upload_custom_emoji', 'delete_custom_emoji', 'set_admin_password', 'set_stream_keys', 'set_extra_page_content', 'set_stream_title', 'set_server_welcome_message', 'set_chat_disabled', 'set_chat_join_messages_enabled', 'set_enable_established_chat_user_mode', 'set_forbidden_username_list', 'set_suggested_username_list', 'set_chat_spam_protection_enabled', 'set_chat_slur_filter_enabled', 'set_chat_require_authentication', 'set_video_codec', 'set_stream_latency_level', 'set_stream_output_variants', 'set_custom_color_variable_values', 'set_logo', 'set_favicon', 'reset_favicon', 'set_tags', 'set_ffmpeg_path', 'set_web_server_port', 'set_web_server_ip', 'set_rtmpserver_port', 'set_socket_host_override', 'set_video_serving_endpoint', 'set_nsfw', 'set_directory_enabled', 'set_social_handles', 'set_s3_configuration', 'set_server_url', 'set_external_actions', 'set_custom_styles', 'set_custom_javascript', 'set_hide_viewer_count', 'set_disable_search_indexing', 'set_federation_enabled', 'set_federation_activity_private', 'set_federation_show_engagement', 'set_federation_username', 'set_federation_go_live_message', 'set_federation_block_domains', 'set_discord_notification_configuration', 'set_browser_notification_configuration', 'get_webhooks', 'delete_webhook', 'create_webhook', 'get_external_apiusers', 'delete_external_apiuser', 'create_external_apiuser', 'auto_update_options', 'auto_update_start', 'auto_update_force_quit', 'reset_ypregistration', 'get_video_playback_metrics', 'get_prometheus_api', 'post_prometheus_api', 'put_prometheus_api', 'delete_prometheus_api', 'send_federated_message', 'get_federated_actions', 'start_indie_auth_flow', 'handle_indie_auth_redirect', 'handle_indie_auth_endpoint_get', 'handle_indie_auth_endpoint_post', 'register_fediverse_otprequest', 'verify_fediverse_otprequest'"
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_status":
            return client.get_status(**kwargs)
        if action == "get_custom_emoji_list":
            return client.get_custom_emoji_list(**kwargs)
        if action == "get_chat_messages":
            return client.get_chat_messages(**kwargs)
        if action == "register_anonymous_chat_user":
            return client.register_anonymous_chat_user(**kwargs)
        if action == "update_message_visibility":
            return client.update_message_visibility(**kwargs)
        if action == "update_user_enabled":
            return client.update_user_enabled(**kwargs)
        if action == "get_web_config":
            return client.get_web_config(**kwargs)
        if action == "get_ypresponse":
            return client.get_ypresponse(**kwargs)
        if action == "get_all_social_platforms":
            return client.get_all_social_platforms(**kwargs)
        if action == "get_video_stream_output_variants":
            return client.get_video_stream_output_variants(**kwargs)
        if action == "ping":
            return client.ping(**kwargs)
        if action == "remote_follow":
            return client.remote_follow(**kwargs)
        if action == "get_followers":
            return client.get_followers(**kwargs)
        if action == "report_playback_metrics":
            return client.report_playback_metrics(**kwargs)
        if action == "register_for_live_notifications":
            return client.register_for_live_notifications(**kwargs)
        if action == "status_admin":
            return client.status_admin(**kwargs)
        if action == "disconnect_inbound_connection":
            return client.disconnect_inbound_connection(**kwargs)
        if action == "get_server_config":
            return client.get_server_config(**kwargs)
        if action == "get_viewers_over_time":
            return client.get_viewers_over_time(**kwargs)
        if action == "get_active_viewers":
            return client.get_active_viewers(**kwargs)
        if action == "get_hardware_stats":
            return client.get_hardware_stats(**kwargs)
        if action == "get_connected_chat_clients":
            return client.get_connected_chat_clients(**kwargs)
        if action == "get_chat_messages_admin":
            return client.get_chat_messages_admin(**kwargs)
        if action == "update_message_visibility_admin":
            return client.update_message_visibility_admin(**kwargs)
        if action == "update_user_enabled_admin":
            return client.update_user_enabled_admin(**kwargs)
        if action == "get_disabled_users":
            return client.get_disabled_users(**kwargs)
        if action == "ban_ipaddress":
            return client.ban_ipaddress(**kwargs)
        if action == "unban_ipaddress":
            return client.unban_ipaddress(**kwargs)
        if action == "get_ipaddress_bans":
            return client.get_ipaddress_bans(**kwargs)
        if action == "update_user_moderator":
            return client.update_user_moderator(**kwargs)
        if action == "get_moderators":
            return client.get_moderators(**kwargs)
        if action == "get_logs":
            return client.get_logs(**kwargs)
        if action == "get_warnings":
            return client.get_warnings(**kwargs)
        if action == "get_followers_admin":
            return client.get_followers_admin(**kwargs)
        if action == "get_pending_follow_requests":
            return client.get_pending_follow_requests(**kwargs)
        if action == "get_blocked_and_rejected_followers":
            return client.get_blocked_and_rejected_followers(**kwargs)
        if action == "approve_follower":
            return client.approve_follower(**kwargs)
        if action == "upload_custom_emoji":
            return client.upload_custom_emoji(**kwargs)
        if action == "delete_custom_emoji":
            return client.delete_custom_emoji(**kwargs)
        if action == "set_admin_password":
            return client.set_admin_password(**kwargs)
        if action == "set_stream_keys":
            return client.set_stream_keys(**kwargs)
        if action == "set_extra_page_content":
            return client.set_extra_page_content(**kwargs)
        if action == "set_stream_title":
            return client.set_stream_title(**kwargs)
        if action == "set_server_welcome_message":
            return client.set_server_welcome_message(**kwargs)
        if action == "set_chat_disabled":
            return client.set_chat_disabled(**kwargs)
        if action == "set_chat_join_messages_enabled":
            return client.set_chat_join_messages_enabled(**kwargs)
        if action == "set_enable_established_chat_user_mode":
            return client.set_enable_established_chat_user_mode(**kwargs)
        if action == "set_forbidden_username_list":
            return client.set_forbidden_username_list(**kwargs)
        if action == "set_suggested_username_list":
            return client.set_suggested_username_list(**kwargs)
        if action == "set_chat_spam_protection_enabled":
            return client.set_chat_spam_protection_enabled(**kwargs)
        if action == "set_chat_slur_filter_enabled":
            return client.set_chat_slur_filter_enabled(**kwargs)
        if action == "set_chat_require_authentication":
            return client.set_chat_require_authentication(**kwargs)
        if action == "set_video_codec":
            return client.set_video_codec(**kwargs)
        if action == "set_stream_latency_level":
            return client.set_stream_latency_level(**kwargs)
        if action == "set_stream_output_variants":
            return client.set_stream_output_variants(**kwargs)
        if action == "set_custom_color_variable_values":
            return client.set_custom_color_variable_values(**kwargs)
        if action == "set_logo":
            return client.set_logo(**kwargs)
        if action == "set_favicon":
            return client.set_favicon(**kwargs)
        if action == "reset_favicon":
            return client.reset_favicon(**kwargs)
        if action == "set_tags":
            return client.set_tags(**kwargs)
        if action == "set_ffmpeg_path":
            return client.set_ffmpeg_path(**kwargs)
        if action == "set_web_server_port":
            return client.set_web_server_port(**kwargs)
        if action == "set_web_server_ip":
            return client.set_web_server_ip(**kwargs)
        if action == "set_rtmpserver_port":
            return client.set_rtmpserver_port(**kwargs)
        if action == "set_socket_host_override":
            return client.set_socket_host_override(**kwargs)
        if action == "set_video_serving_endpoint":
            return client.set_video_serving_endpoint(**kwargs)
        if action == "set_nsfw":
            return client.set_nsfw(**kwargs)
        if action == "set_directory_enabled":
            return client.set_directory_enabled(**kwargs)
        if action == "set_social_handles":
            return client.set_social_handles(**kwargs)
        if action == "set_s3_configuration":
            return client.set_s3_configuration(**kwargs)
        if action == "set_server_url":
            return client.set_server_url(**kwargs)
        if action == "set_external_actions":
            return client.set_external_actions(**kwargs)
        if action == "set_custom_styles":
            return client.set_custom_styles(**kwargs)
        if action == "set_custom_javascript":
            return client.set_custom_javascript(**kwargs)
        if action == "set_hide_viewer_count":
            return client.set_hide_viewer_count(**kwargs)
        if action == "set_disable_search_indexing":
            return client.set_disable_search_indexing(**kwargs)
        if action == "set_federation_enabled":
            return client.set_federation_enabled(**kwargs)
        if action == "set_federation_activity_private":
            return client.set_federation_activity_private(**kwargs)
        if action == "set_federation_show_engagement":
            return client.set_federation_show_engagement(**kwargs)
        if action == "set_federation_username":
            return client.set_federation_username(**kwargs)
        if action == "set_federation_go_live_message":
            return client.set_federation_go_live_message(**kwargs)
        if action == "set_federation_block_domains":
            return client.set_federation_block_domains(**kwargs)
        if action == "set_discord_notification_configuration":
            return client.set_discord_notification_configuration(**kwargs)
        if action == "set_browser_notification_configuration":
            return client.set_browser_notification_configuration(**kwargs)
        if action == "get_webhooks":
            return client.get_webhooks(**kwargs)
        if action == "delete_webhook":
            return client.delete_webhook(**kwargs)
        if action == "create_webhook":
            return client.create_webhook(**kwargs)
        if action == "get_external_apiusers":
            return client.get_external_apiusers(**kwargs)
        if action == "delete_external_apiuser":
            return client.delete_external_apiuser(**kwargs)
        if action == "create_external_apiuser":
            return client.create_external_apiuser(**kwargs)
        if action == "auto_update_options":
            return client.auto_update_options(**kwargs)
        if action == "auto_update_start":
            return client.auto_update_start(**kwargs)
        if action == "auto_update_force_quit":
            return client.auto_update_force_quit(**kwargs)
        if action == "reset_ypregistration":
            return client.reset_ypregistration(**kwargs)
        if action == "get_video_playback_metrics":
            return client.get_video_playback_metrics(**kwargs)
        if action == "get_prometheus_api":
            return client.get_prometheus_api(**kwargs)
        if action == "post_prometheus_api":
            return client.post_prometheus_api(**kwargs)
        if action == "put_prometheus_api":
            return client.put_prometheus_api(**kwargs)
        if action == "delete_prometheus_api":
            return client.delete_prometheus_api(**kwargs)
        if action == "send_federated_message":
            return client.send_federated_message(**kwargs)
        if action == "get_federated_actions":
            return client.get_federated_actions(**kwargs)
        if action == "start_indie_auth_flow":
            return client.start_indie_auth_flow(**kwargs)
        if action == "handle_indie_auth_redirect":
            return client.handle_indie_auth_redirect(**kwargs)
        if action == "handle_indie_auth_endpoint_get":
            return client.handle_indie_auth_endpoint_get(**kwargs)
        if action == "handle_indie_auth_endpoint_post":
            return client.handle_indie_auth_endpoint_post(**kwargs)
        if action == "register_fediverse_otprequest":
            return client.register_fediverse_otprequest(**kwargs)
        if action == "verify_fediverse_otprequest":
            return client.verify_fediverse_otprequest(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_objects_tools(mcp: FastMCP):
    @mcp.tool(tags={"objects"})
    async def owncast_objects(
        action: str = Field(
            description="Action to perform. Must be one of: 'set_server_name', 'set_server_summary', 'set_custom_offline_message'"
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "set_server_name":
            return client.set_server_name(**kwargs)
        if action == "set_server_summary":
            return client.set_server_summary(**kwargs)
        if action == "set_custom_offline_message":
            return client.set_custom_offline_message(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_external_tools(mcp: FastMCP):
    @mcp.tool(tags={"external"})
    async def owncast_external(
        action: str = Field(
            description="Action to perform. Must be one of: 'send_system_message', 'send_system_message_to_connected_client', 'send_user_message', 'send_integration_chat_message', 'send_chat_action', 'external_update_message_visibility', 'external_get_status', 'external_set_stream_title', 'external_get_chat_messages', 'external_get_connected_chat_clients', 'external_get_user_details'"
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "send_system_message":
            return client.send_system_message(**kwargs)
        if action == "send_system_message_to_connected_client":
            return client.send_system_message_to_connected_client(**kwargs)
        if action == "send_user_message":
            return client.send_user_message(**kwargs)
        if action == "send_integration_chat_message":
            return client.send_integration_chat_message(**kwargs)
        if action == "send_chat_action":
            return client.send_chat_action(**kwargs)
        if action == "external_update_message_visibility":
            return client.external_update_message_visibility(**kwargs)
        if action == "external_get_status":
            return client.external_get_status(**kwargs)
        if action == "external_set_stream_title":
            return client.external_set_stream_title(**kwargs)
        if action == "external_get_chat_messages":
            return client.external_get_chat_messages(**kwargs)
        if action == "external_get_connected_chat_clients":
            return client.external_get_connected_chat_clients(**kwargs)
        if action == "external_get_user_details":
            return client.external_get_user_details(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_chat_tools(mcp: FastMCP):
    @mcp.tool(tags={"chat"})
    async def owncast_chat(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_user_details'"
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_user_details":
            return client.get_user_details(**kwargs)
        raise ValueError(f"Unknown action: {action}")


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
