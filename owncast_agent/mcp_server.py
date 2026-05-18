#!/usr/bin/python
import warnings

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
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from owncast_agent.auth import get_client

__version__ = "0.11.0"

logger = get_logger(name="owncast-agent")
logger.setLevel(logging.INFO)


def register_internal_tools(mcp: FastMCP):
    @mcp.tool(tags={"internal"})
    async def owncast_internal(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_status', 'get_custom_emoji_list', 'get_chat_messages', 'register_anonymous_chat_user', 'update_message_visibility', 'update_user_enabled', 'get_web_config', 'get_ypresponse', 'get_all_social_platforms', 'get_video_stream_output_variants', 'ping', 'remote_follow', 'get_followers', 'report_playback_metrics', 'register_for_live_notifications', 'status_admin', 'disconnect_inbound_connection', 'get_server_config', 'get_viewers_over_time', 'get_active_viewers', 'get_hardware_stats', 'get_connected_chat_clients', 'get_chat_messages_admin', 'update_message_visibility_admin', 'update_user_enabled_admin', 'get_disabled_users', 'ban_ipaddress', 'unban_ipaddress', 'get_ipaddress_bans', 'update_user_moderator', 'get_moderators', 'get_logs', 'get_warnings', 'get_followers_admin', 'get_pending_follow_requests', 'get_blocked_and_rejected_followers', 'approve_follower', 'upload_custom_emoji', 'delete_custom_emoji', 'set_admin_password', 'set_stream_keys', 'set_extra_page_content', 'set_stream_title', 'set_server_welcome_message', 'set_chat_disabled', 'set_chat_join_messages_enabled', 'set_enable_established_chat_user_mode', 'set_forbidden_username_list', 'set_suggested_username_list', 'set_chat_spam_protection_enabled', 'set_chat_slur_filter_enabled', 'set_chat_require_authentication', 'set_video_codec', 'set_stream_latency_level', 'set_stream_output_variants', 'set_custom_color_variable_values', 'set_logo', 'set_favicon', 'reset_favicon', 'set_tags', 'set_ffmpeg_path', 'set_web_server_port', 'set_web_server_ip', 'set_rtmpserver_port', 'set_socket_host_override', 'set_video_serving_endpoint', 'set_nsfw', 'set_directory_enabled', 'set_social_handles', 'set_s3_configuration', 'set_server_url', 'set_external_actions', 'set_custom_styles', 'set_custom_javascript', 'set_hide_viewer_count', 'set_disable_search_indexing', 'set_federation_enabled', 'set_federation_activity_private', 'set_federation_show_engagement', 'set_federation_username', 'set_federation_go_live_message', 'set_federation_block_domains', 'set_discord_notification_configuration', 'set_browser_notification_configuration', 'get_webhooks', 'delete_webhook', 'create_webhook', 'get_external_apiusers', 'delete_external_apiuser', 'create_external_apiuser', 'auto_update_options', 'auto_update_start', 'auto_update_force_quit', 'reset_ypregistration', 'get_video_playback_metrics', 'get_prometheus_api', 'post_prometheus_api', 'put_prometheus_api', 'delete_prometheus_api', 'send_federated_message', 'get_federated_actions', 'start_indie_auth_flow', 'handle_indie_auth_redirect', 'handle_indie_auth_endpoint_get', 'handle_indie_auth_endpoint_post', 'register_fediverse_otprequest', 'verify_fediverse_otprequest'"
        ),
        access_token: str | None = Field(default=None, description="access token"),
        x_forwarded_user: str | None = Field(
            default=None, description="x forwarded user"
        ),
        display_name: str | None = Field(default=None, description="display name"),
        body: dict | None = Field(default=None, description="body"),
        user_id: str | None = Field(default=None, description="user id"),
        enabled: bool | None = Field(default=None, description="enabled"),
        account: str | None = Field(default=None, description="account"),
        offset: int | None = Field(default=None, description="offset"),
        limit: int | None = Field(default=None, description="limit"),
        channel: str | None = Field(default=None, description="channel"),
        destination: str | None = Field(default=None, description="destination"),
        window_start: str | None = Field(default=None, description="window start"),
        is_moderator: bool | None = Field(default=None, description="is moderator"),
        actor_iri: str | None = Field(default=None, description="actor iri"),
        approved: bool | None = Field(default=None, description="approved"),
        name: str | None = Field(default=None, description="name"),
        data: str | None = Field(default=None, description="data"),
        value: Any | None = Field(default=None, description="value"),
        id: int | None = Field(default=None, description="id"),
        url: str | None = Field(default=None, description="url"),
        events: list | None = Field(default=None, description="events"),
        token: str | None = Field(default=None, description="token"),
        scopes: list | None = Field(default=None, description="scopes"),
        auth_host: str | None = Field(default=None, description="auth host"),
        state: str | None = Field(default=None, description="state"),
        client_id: str | None = Field(default=None, description="client id"),
        redirect_uri: str | None = Field(default=None, description="redirect uri"),
        code_challenge: str | None = Field(default=None, description="code challenge"),
        code: str | None = Field(default=None, description="code"),
        client=Depends(get_client),
    ) -> dict:
        """Manage internal operations.

        Actions:
          - 'get_status': Get the status of the server
          - 'get_custom_emoji_list': Get list of custom emojis supported in the chat
          - 'get_chat_messages': Gets a list of chat messages
          - 'register_anonymous_chat_user': Registers an anonymous chat user
          - 'update_message_visibility': Update chat message visibility
          - 'update_user_enabled': Enable/disable a user
          - 'get_web_config': Get the web config
          - 'get_ypresponse': Get the YP protocol data
          - 'get_all_social_platforms': Get all social platforms
          - 'get_video_stream_output_variants': Get a list of video variants available
          - 'ping': Tell the backend you're an active viewer
          - 'remote_follow': Request remote follow
          - 'get_followers': Gets the list of followers
          - 'report_playback_metrics': Save video playback metrics for future video health recording
          - 'register_for_live_notifications': Register for notifications
          - 'status_admin': Get current inboard broadcaster
          - 'disconnect_inbound_connection': Disconnect inbound stream
          - 'get_server_config': Get the current server config
          - 'get_viewers_over_time': Get viewer count over time
          - 'get_active_viewers': Get active viewers
          - 'get_hardware_stats': Get the current hardware stats
          - 'get_connected_chat_clients': Get a detailed list of currently connected chat clients
          - 'get_chat_messages_admin': Get all chat messages for the admin, unfiltered
          - 'update_message_visibility_admin': Update visibility of chat messages
          - 'update_user_enabled_admin': Enable or disable a user
          - 'get_disabled_users': Get a list of disabled users
          - 'ban_ipaddress': Ban an IP address
          - 'unban_ipaddress': Remove an IP ban
          - 'get_ipaddress_bans': Get all banned IP addresses
          - 'update_user_moderator': Set moderator status for a user
          - 'get_moderators': Get a list of moderator users
          - 'get_logs': Get all logs
          - 'get_warnings': Get warning/error logs
          - 'get_followers_admin': Get followers
          - 'get_pending_follow_requests': Get a list of pending follow requests
          - 'get_blocked_and_rejected_followers': Get a list of rejected or blocked follows
          - 'approve_follower': Set the following state of a follower or follow request
          - 'upload_custom_emoji': Upload custom emoji
          - 'delete_custom_emoji': Delete custom emoji
          - 'set_admin_password': Change the current admin password
          - 'set_stream_keys': Set an array of valid stream keys
          - 'set_extra_page_content': Change the extra page content in memory
          - 'set_stream_title': Change the stream title
          - 'set_server_welcome_message': Change the welcome message
          - 'set_chat_disabled': Disable chat
          - 'set_chat_join_messages_enabled': Enable chat for user join messages
          - 'set_enable_established_chat_user_mode': Enable/disable chat established user mode
          - 'set_forbidden_username_list': Set chat usernames that are not allowed
          - 'set_suggested_username_list': Set the suggested chat usernames that will be assigned automatically
          - 'set_chat_spam_protection_enabled': Set spam protection enabled
          - 'set_chat_slur_filter_enabled': Set slur filter enabled
          - 'set_chat_require_authentication': Set require authentication for chat
          - 'set_video_codec': Set video codec
          - 'set_stream_latency_level': Set the number of video segments and duration per segment in a playlist
          - 'set_stream_output_variants': Set an array of video output configurations
          - 'set_custom_color_variable_values': Set style/color/css values
          - 'set_logo': Update logo
          - 'set_favicon': Upload custom favicon
          - 'reset_favicon': Reset favicon to default
          - 'set_tags': Update server tags
          - 'set_ffmpeg_path': Update FFMPEG path
          - 'set_web_server_port': Update server port
          - 'set_web_server_ip': Update server IP address
          - 'set_rtmpserver_port': Update RTMP post
          - 'set_socket_host_override': Update websocket host override
          - 'set_video_serving_endpoint': Update custom video serving endpoint
          - 'set_nsfw': Update NSFW marking
          - 'set_directory_enabled': Update directory enabled
          - 'set_social_handles': Update social handles
          - 'set_s3_configuration': Update S3 configuration
          - 'set_server_url': Update server url
          - 'set_external_actions': Update external action links
          - 'set_custom_styles': Update custom styles
          - 'set_custom_javascript': Update custom JavaScript
          - 'set_hide_viewer_count': Update hide viewer count
          - 'set_disable_search_indexing': Update search indexing
          - 'set_federation_enabled': Enable/disable federation features
          - 'set_federation_activity_private': Set if federation activities are private
          - 'set_federation_show_engagement': Set if fediverse engagement appears in chat
          - 'set_federation_username': Set local federated username
          - 'set_federation_go_live_message': Set federated go live message
          - 'set_federation_block_domains': Set Federation blocked domains
          - 'set_discord_notification_configuration': Configure Discord notifications
          - 'set_browser_notification_configuration': Configure Browser notifications
          - 'get_webhooks': Get all the webhooks
          - 'delete_webhook': Delete a single webhook
          - 'create_webhook': Create a single webhook
          - 'get_external_apiusers': Get all access tokens
          - 'delete_external_apiuser': Delete a single external API user
          - 'create_external_apiuser': Create a single access token
          - 'auto_update_options': Return the auto-update features that are supported for this instance
          - 'auto_update_start': Begin the auto-update
          - 'auto_update_force_quit': Force quit the server and restart it
          - 'reset_ypregistration': Reset YP configuration
          - 'get_video_playback_metrics': Get video playback metrics
          - 'get_prometheus_api': Endpoint to interface with Prometheus
          - 'post_prometheus_api': Endpoint to interface with Prometheus
          - 'put_prometheus_api': Endpoint to interface with Prometheus
          - 'delete_prometheus_api': Endpoint to interface with Prometheus
          - 'send_federated_message': Send a public message to the Fediverse from the server's user
          - 'get_federated_actions': Get a paginated list of federated activities
          - 'start_indie_auth_flow': Begins auth flow
          - 'handle_indie_auth_redirect': Handle the redirect from an IndieAuth server to continue the auth flow
          - 'handle_indie_auth_endpoint_get': Handles the IndieAuth auth endpoint
          - 'handle_indie_auth_endpoint_post': Handles IndieAuth from form submission
          - 'register_fediverse_otprequest': Register a Fediverse OTP request
          - 'verify_fediverse_otprequest': Verify Fediverse OTP code
        """
        kwargs: dict[str, Any]
        if action == "get_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_status(**kwargs)
        if action == "get_custom_emoji_list":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_custom_emoji_list(**kwargs)
        if action == "get_chat_messages":
            kwargs = {"access_token": access_token}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_chat_messages(**kwargs)
        if action == "register_anonymous_chat_user":
            kwargs = {
                "x_forwarded_user": x_forwarded_user,
                "display_name": display_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.register_anonymous_chat_user(**kwargs)
        if action == "update_message_visibility":
            kwargs = {"access_token": access_token, "body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_message_visibility(**kwargs)
        if action == "update_user_enabled":
            kwargs = {
                "access_token": access_token,
                "user_id": user_id,
                "enabled": enabled,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_user_enabled(**kwargs)
        if action == "get_web_config":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_web_config(**kwargs)
        if action == "get_ypresponse":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_ypresponse(**kwargs)
        if action == "get_all_social_platforms":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_all_social_platforms(**kwargs)
        if action == "get_video_stream_output_variants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_video_stream_output_variants(**kwargs)
        if action == "ping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.ping(**kwargs)
        if action == "remote_follow":
            kwargs = {"account": account}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.remote_follow(**kwargs)
        if action == "get_followers":
            kwargs = {"offset": offset, "limit": limit}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_followers(**kwargs)
        if action == "report_playback_metrics":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.report_playback_metrics(**kwargs)
        if action == "register_for_live_notifications":
            kwargs = {
                "access_token": access_token,
                "channel": channel,
                "destination": destination,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.register_for_live_notifications(**kwargs)
        if action == "status_admin":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.status_admin(**kwargs)
        if action == "disconnect_inbound_connection":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.disconnect_inbound_connection(**kwargs)
        if action == "get_server_config":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_server_config(**kwargs)
        if action == "get_viewers_over_time":
            kwargs = {"window_start": window_start}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_viewers_over_time(**kwargs)
        if action == "get_active_viewers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_active_viewers(**kwargs)
        if action == "get_hardware_stats":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_hardware_stats(**kwargs)
        if action == "get_connected_chat_clients":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_connected_chat_clients(**kwargs)
        if action == "get_chat_messages_admin":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_chat_messages_admin(**kwargs)
        if action == "update_message_visibility_admin":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_message_visibility_admin(**kwargs)
        if action == "update_user_enabled_admin":
            kwargs = {"user_id": user_id, "enabled": enabled}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_user_enabled_admin(**kwargs)
        if action == "get_disabled_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_disabled_users(**kwargs)
        if action == "ban_ipaddress":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.ban_ipaddress(**kwargs)
        if action == "unban_ipaddress":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.unban_ipaddress(**kwargs)
        if action == "get_ipaddress_bans":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_ipaddress_bans(**kwargs)
        if action == "update_user_moderator":
            kwargs = {"user_id": user_id, "is_moderator": is_moderator}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_user_moderator(**kwargs)
        if action == "get_moderators":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_moderators(**kwargs)
        if action == "get_logs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_logs(**kwargs)
        if action == "get_warnings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_warnings(**kwargs)
        if action == "get_followers_admin":
            kwargs = {"offset": offset, "limit": limit}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_followers_admin(**kwargs)
        if action == "get_pending_follow_requests":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_pending_follow_requests(**kwargs)
        if action == "get_blocked_and_rejected_followers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_blocked_and_rejected_followers(**kwargs)
        if action == "approve_follower":
            kwargs = {"actor_iri": actor_iri, "approved": approved}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.approve_follower(**kwargs)
        if action == "upload_custom_emoji":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upload_custom_emoji(**kwargs)
        if action == "delete_custom_emoji":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_custom_emoji(**kwargs)
        if action == "set_admin_password":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_admin_password(**kwargs)
        if action == "set_stream_keys":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_stream_keys(**kwargs)
        if action == "set_extra_page_content":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_extra_page_content(**kwargs)
        if action == "set_stream_title":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_stream_title(**kwargs)
        if action == "set_server_welcome_message":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_server_welcome_message(**kwargs)
        if action == "set_chat_disabled":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_chat_disabled(**kwargs)
        if action == "set_chat_join_messages_enabled":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_chat_join_messages_enabled(**kwargs)
        if action == "set_enable_established_chat_user_mode":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_enable_established_chat_user_mode(**kwargs)
        if action == "set_forbidden_username_list":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_forbidden_username_list(**kwargs)
        if action == "set_suggested_username_list":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_suggested_username_list(**kwargs)
        if action == "set_chat_spam_protection_enabled":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_chat_spam_protection_enabled(**kwargs)
        if action == "set_chat_slur_filter_enabled":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_chat_slur_filter_enabled(**kwargs)
        if action == "set_chat_require_authentication":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_chat_require_authentication(**kwargs)
        if action == "set_video_codec":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_video_codec(**kwargs)
        if action == "set_stream_latency_level":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_stream_latency_level(**kwargs)
        if action == "set_stream_output_variants":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_stream_output_variants(**kwargs)
        if action == "set_custom_color_variable_values":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_custom_color_variable_values(**kwargs)
        if action == "set_logo":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_logo(**kwargs)
        if action == "set_favicon":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_favicon(**kwargs)
        if action == "reset_favicon":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.reset_favicon(**kwargs)
        if action == "set_tags":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_tags(**kwargs)
        if action == "set_ffmpeg_path":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_ffmpeg_path(**kwargs)
        if action == "set_web_server_port":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_web_server_port(**kwargs)
        if action == "set_web_server_ip":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_web_server_ip(**kwargs)
        if action == "set_rtmpserver_port":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_rtmpserver_port(**kwargs)
        if action == "set_socket_host_override":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_socket_host_override(**kwargs)
        if action == "set_video_serving_endpoint":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_video_serving_endpoint(**kwargs)
        if action == "set_nsfw":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_nsfw(**kwargs)
        if action == "set_directory_enabled":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_directory_enabled(**kwargs)
        if action == "set_social_handles":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_social_handles(**kwargs)
        if action == "set_s3_configuration":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_s3_configuration(**kwargs)
        if action == "set_server_url":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_server_url(**kwargs)
        if action == "set_external_actions":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_external_actions(**kwargs)
        if action == "set_custom_styles":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_custom_styles(**kwargs)
        if action == "set_custom_javascript":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_custom_javascript(**kwargs)
        if action == "set_hide_viewer_count":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_hide_viewer_count(**kwargs)
        if action == "set_disable_search_indexing":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_disable_search_indexing(**kwargs)
        if action == "set_federation_enabled":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_federation_enabled(**kwargs)
        if action == "set_federation_activity_private":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_federation_activity_private(**kwargs)
        if action == "set_federation_show_engagement":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_federation_show_engagement(**kwargs)
        if action == "set_federation_username":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_federation_username(**kwargs)
        if action == "set_federation_go_live_message":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_federation_go_live_message(**kwargs)
        if action == "set_federation_block_domains":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_federation_block_domains(**kwargs)
        if action == "set_discord_notification_configuration":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_discord_notification_configuration(**kwargs)
        if action == "set_browser_notification_configuration":
            kwargs = {"value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_browser_notification_configuration(**kwargs)
        if action == "get_webhooks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_webhooks(**kwargs)
        if action == "delete_webhook":
            kwargs = {"id": id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_webhook(**kwargs)
        if action == "create_webhook":
            kwargs = {"url": url, "events": events}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_webhook(**kwargs)
        if action == "get_external_apiusers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_external_apiusers(**kwargs)
        if action == "delete_external_apiuser":
            kwargs = {"token": token}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_external_apiuser(**kwargs)
        if action == "create_external_apiuser":
            kwargs = {"name": name, "scopes": scopes}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_external_apiuser(**kwargs)
        if action == "auto_update_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.auto_update_options(**kwargs)
        if action == "auto_update_start":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.auto_update_start(**kwargs)
        if action == "auto_update_force_quit":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.auto_update_force_quit(**kwargs)
        if action == "reset_ypregistration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.reset_ypregistration(**kwargs)
        if action == "get_video_playback_metrics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_video_playback_metrics(**kwargs)
        if action == "get_prometheus_api":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_prometheus_api(**kwargs)
        if action == "post_prometheus_api":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_prometheus_api(**kwargs)
        if action == "put_prometheus_api":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_prometheus_api(**kwargs)
        if action == "delete_prometheus_api":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_prometheus_api(**kwargs)
        if action == "send_federated_message":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.send_federated_message(**kwargs)
        if action == "get_federated_actions":
            kwargs = {"offset": offset, "limit": limit}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_federated_actions(**kwargs)
        if action == "start_indie_auth_flow":
            kwargs = {
                "access_token": access_token,
                "auth_host": auth_host,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.start_indie_auth_flow(**kwargs)
        if action == "handle_indie_auth_redirect":
            kwargs = {"state": state}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.handle_indie_auth_redirect(**kwargs)
        if action == "handle_indie_auth_endpoint_get":
            kwargs = {
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "code_challenge": code_challenge,
                "state": state,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.handle_indie_auth_endpoint_get(**kwargs)
        if action == "handle_indie_auth_endpoint_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.handle_indie_auth_endpoint_post(**kwargs)
        if action == "register_fediverse_otprequest":
            kwargs = {"access_token": access_token, "account": account}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.register_fediverse_otprequest(**kwargs)
        if action == "verify_fediverse_otprequest":
            kwargs = {"code": code}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.verify_fediverse_otprequest(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_status', 'get_custom_emoji_list', 'get_chat_messages', 'register_anonymous_chat_user', 'update_message_visibility', 'update_user_enabled', 'get_web_config', 'get_ypresponse', 'get_all_social_platforms', 'get_video_stream_output_variants', 'ping', 'remote_follow', 'get_followers', 'report_playback_metrics', 'register_for_live_notifications', 'status_admin', 'disconnect_inbound_connection', 'get_server_config', 'get_viewers_over_time', 'get_active_viewers', 'get_hardware_stats', 'get_connected_chat_clients', 'get_chat_messages_admin', 'update_message_visibility_admin', 'update_user_enabled_admin', 'get_disabled_users', 'ban_ipaddress', 'unban_ipaddress', 'get_ipaddress_bans', 'update_user_moderator', 'get_moderators', 'get_logs', 'get_warnings', 'get_followers_admin', 'get_pending_follow_requests', 'get_blocked_and_rejected_followers', 'approve_follower', 'upload_custom_emoji', 'delete_custom_emoji', 'set_admin_password', 'set_stream_keys', 'set_extra_page_content', 'set_stream_title', 'set_server_welcome_message', 'set_chat_disabled', 'set_chat_join_messages_enabled', 'set_enable_established_chat_user_mode', 'set_forbidden_username_list', 'set_suggested_username_list', 'set_chat_spam_protection_enabled', 'set_chat_slur_filter_enabled', 'set_chat_require_authentication', 'set_video_codec', 'set_stream_latency_level', 'set_stream_output_variants', 'set_custom_color_variable_values', 'set_logo', 'set_favicon', 'reset_favicon', 'set_tags', 'set_ffmpeg_path', 'set_web_server_port', 'set_web_server_ip', 'set_rtmpserver_port', 'set_socket_host_override', 'set_video_serving_endpoint', 'set_nsfw', 'set_directory_enabled', 'set_social_handles', 'set_s3_configuration', 'set_server_url', 'set_external_actions', 'set_custom_styles', 'set_custom_javascript', 'set_hide_viewer_count', 'set_disable_search_indexing', 'set_federation_enabled', 'set_federation_activity_private', 'set_federation_show_engagement', 'set_federation_username', 'set_federation_go_live_message', 'set_federation_block_domains', 'set_discord_notification_configuration', 'set_browser_notification_configuration', 'get_webhooks', 'delete_webhook', 'create_webhook', 'get_external_apiusers', 'delete_external_apiuser', 'create_external_apiuser', 'auto_update_options', 'auto_update_start', 'auto_update_force_quit', 'reset_ypregistration', 'get_video_playback_metrics', 'get_prometheus_api', 'post_prometheus_api', 'put_prometheus_api', 'delete_prometheus_api', 'send_federated_message', 'get_federated_actions', 'start_indie_auth_flow', 'handle_indie_auth_redirect', 'handle_indie_auth_endpoint_get', 'handle_indie_auth_endpoint_post', 'register_fediverse_otprequest', 'verify_fediverse_otprequest"
        )


def register_objects_tools(mcp: FastMCP):
    @mcp.tool(tags={"objects"})
    async def owncast_objects(
        action: str = Field(
            description="Action to perform. Must be one of: 'set_server_name', 'set_server_summary', 'set_custom_offline_message'"
        ),
        body: dict | None = Field(default=None, description="body"),
        client=Depends(get_client),
    ) -> dict:
        """Manage objects operations.

        Actions:
          - 'set_server_name': Change the server name
          - 'set_server_summary': Change the server summary
          - 'set_custom_offline_message': Change the offline message
        """
        kwargs: dict[str, Any]
        if action == "set_server_name":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_server_name(**kwargs)
        if action == "set_server_summary":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_server_summary(**kwargs)
        if action == "set_custom_offline_message":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_custom_offline_message(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: set_server_name', 'set_server_summary', 'set_custom_offline_message"
        )


def register_external_tools(mcp: FastMCP):
    @mcp.tool(tags={"external"})
    async def owncast_external(
        action: str = Field(
            description="Action to perform. Must be one of: 'send_system_message', 'send_system_message_to_connected_client', 'send_user_message', 'send_integration_chat_message', 'send_chat_action', 'external_update_message_visibility', 'external_get_status', 'external_set_stream_title', 'external_get_chat_messages', 'external_get_connected_chat_clients', 'external_get_user_details'"
        ),
        body: dict | None = Field(default=None, description="body"),
        client_id: int | None = Field(default=None, description="client id"),
        user_id: str | None = Field(default=None, description="user id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage external operations.

        Actions:
          - 'send_system_message': Send a system message to the chat
          - 'send_system_message_to_connected_client': Send a system message to a single client
          - 'send_user_message': Send a user message to chat
          - 'send_integration_chat_message': Send a message to chat as a specific 3rd party bot/integration based on its access token
          - 'send_chat_action': Send a user action to chat
          - 'external_update_message_visibility': Hide chat message
          - 'external_get_status': Get the server's status
          - 'external_set_stream_title': Stream title
          - 'external_get_chat_messages': Get chat history
          - 'external_get_connected_chat_clients': Connected clients
          - 'external_get_user_details': Get a user's details
        """
        kwargs: dict[str, Any]
        if action == "send_system_message":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.send_system_message(**kwargs)
        if action == "send_system_message_to_connected_client":
            kwargs = {"client_id": client_id, "body": body}  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.send_system_message_to_connected_client(**kwargs)
        if action == "send_user_message":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.send_user_message(**kwargs)
        if action == "send_integration_chat_message":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.send_integration_chat_message(**kwargs)
        if action == "send_chat_action":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.send_chat_action(**kwargs)
        if action == "external_update_message_visibility":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.external_update_message_visibility(**kwargs)
        if action == "external_get_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.external_get_status(**kwargs)
        if action == "external_set_stream_title":
            kwargs = {"body": body}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.external_set_stream_title(**kwargs)
        if action == "external_get_chat_messages":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.external_get_chat_messages(**kwargs)
        if action == "external_get_connected_chat_clients":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.external_get_connected_chat_clients(**kwargs)
        if action == "external_get_user_details":
            kwargs = {"user_id": user_id}  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.external_get_user_details(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: send_system_message', 'send_system_message_to_connected_client', 'send_user_message', 'send_integration_chat_message', 'send_chat_action', 'external_update_message_visibility', 'external_get_status', 'external_set_stream_title', 'external_get_chat_messages', 'external_get_connected_chat_clients', 'external_get_user_details"
        )


def register_chat_tools(mcp: FastMCP):
    @mcp.tool(tags={"chat"})
    async def owncast_chat(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_user_details'"
        ),
        user_id: str | None = Field(default=None, description="user id"),
        access_token: str | None = Field(default=None, description="access token"),
        client=Depends(get_client),
    ) -> dict:
        """Manage chat operations.

        Actions:
          - 'get_user_details': Get a user's details
        """
        kwargs: dict[str, Any]
        if action == "get_user_details":
            kwargs = {"user_id": user_id, "access_token": access_token}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_details(**kwargs)
        raise ValueError(f"Unknown action: {action}. Must be one of: get_user_details")


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
