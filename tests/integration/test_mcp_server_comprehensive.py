import importlib
import sys

# Set dummy sys.argv before importing anything to prevent create_mcp_server parsing issues
sys.argv = ["mcp_server.py"]

import json
from unittest.mock import MagicMock, patch

import pytest

from owncast_agent.mcp_server import get_mcp_instance, mcp_server


@pytest.mark.asyncio
@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
async def test_mcp_health_check():
    """Verify that the FastMCP health check endpoint behaves correctly by capturing the custom_route decorator.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    captured_routes = {}

    def mock_custom_route(path, methods=None):
        def decorator(f):
            captured_routes[path] = f
            return f

        return decorator

    # Patch FastMCP's custom_route method to capture the local health_check function
    with patch("fastmcp.FastMCP.custom_route", side_effect=mock_custom_route):
        mcp, _, _ = get_mcp_instance()

    # Trigger captured health_check route
    assert "/health" in captured_routes
    mock_request = MagicMock()
    response = await captured_routes["/health"](mock_request)
    assert response.status_code == 200
    assert json.loads(response.body.decode("utf-8")) == {"status": "OK"}


@pytest.mark.asyncio
@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
async def test_mcp_tools_routing(mock_client):
    """Test all mcp tools programmatically and verify all action branches.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    mcp, _, _ = get_mcp_instance()

    # Retrieve all tools registered on FastMCP
    tools = await mcp.list_tools()

    # Extract lists of actions for each tool to ensure 100% conditional branch coverage
    internal_actions = [
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
    ]

    objects_actions = [
        "set_server_name",
        "set_server_summary",
        "set_custom_offline_message",
    ]

    external_actions = [
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
    ]

    chat_actions = ["get_user_details"]

    for tool in tools:
        # Test each possible action string to hit the individual routing branches
        if tool.name == "owncast_internal":
            for act in internal_actions:
                res = await tool.fn(
                    action=act, params_json='{"arg": 1}', client=mock_client, ctx=None
                )
                assert res.get("status") == "success"
            with pytest.raises(ValueError):
                await tool.fn(
                    action="unknown_internal_action",
                    params_json="{}",
                    client=mock_client,
                    ctx=None,
                )

        elif tool.name == "owncast_objects":
            for act in objects_actions:
                res = await tool.fn(
                    action=act, params_json='{"arg": 1}', client=mock_client, ctx=None
                )
                assert res.get("status") == "success"
            with pytest.raises(ValueError):
                await tool.fn(
                    action="unknown_object_action",
                    params_json="{}",
                    client=mock_client,
                    ctx=None,
                )

        elif tool.name == "owncast_external":
            for act in external_actions:
                res = await tool.fn(
                    action=act, params_json='{"arg": 1}', client=mock_client, ctx=None
                )
                assert res.get("status") == "success"
            with pytest.raises(ValueError):
                await tool.fn(
                    action="unknown_external_action",
                    params_json="{}",
                    client=mock_client,
                    ctx=None,
                )

        elif tool.name == "owncast_chat":
            for act in chat_actions:
                res = await tool.fn(
                    action=act, params_json='{"arg": 1}', client=mock_client, ctx=None
                )
                assert res.get("status") == "success"
            with pytest.raises(ValueError):
                await tool.fn(
                    action="unknown_chat_action",
                    params_json="{}",
                    client=mock_client,
                    ctx=None,
                )

        # Test invalid JSON parsing error path
        res_error = await tool.fn(
            action="get_status",
            params_json="{invalid-json",
            client=mock_client,
            ctx=None,
        )
        assert "error" in res_error
        assert "Invalid params_json" in res_error["error"]


@pytest.mark.asyncio
@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
async def test_mcp_context_logging(mock_client):
    """Confirm that passing a FastMCP Context records execution steps correctly.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    mcp, _, _ = get_mcp_instance()
    tools = await mcp.list_tools()

    called_info = []

    async def mock_info(msg):
        called_info.append(msg)

    mock_ctx = MagicMock()
    mock_ctx.info = mock_info
    for tool in tools:
        if tool.name == "owncast_chat":
            await tool.fn(
                action="get_user_details",
                params_json="{}",
                client=mock_client,
                ctx=mock_ctx,
            )
        elif tool.name == "owncast_internal":
            await tool.fn(
                action="get_status", params_json="{}", client=mock_client, ctx=mock_ctx
            )
        elif tool.name == "owncast_objects":
            await tool.fn(
                action="set_server_name",
                params_json='{"name": "test"}',
                client=mock_client,
                ctx=mock_ctx,
            )
        elif tool.name == "owncast_external":
            await tool.fn(
                action="send_system_message",
                params_json='{"body": "test"}',
                client=mock_client,
                ctx=mock_ctx,
            )

    assert len(called_info) > 0


@pytest.mark.concept("AU-ORCH.adapter.kg-graph-materialization")
def test_mcp_server_cli_execution():
    """Verify CLI configuration and server startup transitions for stdio, HTTP, and SSE transports.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    mock_mcp = MagicMock()
    mock_args = MagicMock()
    mock_args.host = "localhost"
    mock_args.port = 8000
    mock_args.auth_type = "none"

    with patch(
        "owncast_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args, []),
    ):
        # 1. Test stdio transport
        mock_args.transport = "stdio"
        mcp_server()
        mock_mcp.run.assert_called_with(transport="stdio")

        # 2. Test streamable-http transport
        mock_args.transport = "streamable-http"
        mcp_server()
        mock_mcp.run.assert_called_with(
            transport="streamable-http", host="localhost", port=8000
        )

        # 3. Test sse transport
        mock_args.transport = "sse"
        mcp_server()
        mock_mcp.run.assert_called_with(transport="sse", host="localhost", port=8000)

        # 4. Test invalid transport (should log error and raise SystemExit)
        mock_args.transport = "invalid-transport"
        with pytest.raises(SystemExit):
            mcp_server()


@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
def test_import_dependency_warning_import_error():
    """Verify handling of RequestsDependencyWarning when requests is missing.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    import sys

    mcp_server_mod = sys.modules["owncast_agent.mcp_server"]
    import builtins

    orig_import = builtins.__import__

    def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "requests.exceptions" or (
            fromlist and "RequestsDependencyWarning" in fromlist
        ):
            raise ImportError("Simulated import error")
        return orig_import(name, globals, locals, fromlist, level)

    with patch("builtins.__import__", side_effect=mock_import):
        try:
            importlib.reload(mcp_server_mod)
        except Exception as e:
            pytest.fail(
                f"Module reload failed under missing requests warning import: {e}"
            )


@pytest.mark.concept("AU-ORCH.adapter.kg-graph-materialization")
def test_mcp_server_main_execution():
    """Verify that calling the module directly runs the server.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    import runpy

    with patch("sys.argv", ["mcp_server.py"]), patch("fastmcp.FastMCP.run") as mock_run:
        runpy.run_module("owncast_agent.mcp_server", run_name="__main__")
        mock_run.assert_called_with(transport="stdio")
