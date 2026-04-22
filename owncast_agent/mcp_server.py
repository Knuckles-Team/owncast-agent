import warnings

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

# General urllib3/chardet mismatch warnings
warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import os
import sys
from typing import Any

from dotenv import find_dotenv, load_dotenv
from fastmcp import FastMCP

__version__ = "0.1.7"

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server

from .auth import get_client

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def register_prompts(mcp: FastMCP):
    @mcp.prompt(
        name="owncast-system-summary",
        description="Get a summary of the Owncast server status",
    )
    def owncast_system_summary() -> str:
        return "Check the current stream status, viewer count, and active configuration for the Owncast instance."


### BEGIN GENERATED TOOL REGISTRATION ###


def register_internal_tools(mcp: FastMCP):
    @mcp.tool(
        name="owncast-internal-get-status",
        description="Get the status of the server",
        tags={"internal"},
    )
    def get_status() -> dict[str, Any]:
        return get_client().get_status()

    @mcp.tool(
        name="owncast-internal-get-custom-emoji-list",
        description="Get list of custom emojis supported in the chat",
        tags={"internal"},
    )
    def get_custom_emoji_list() -> dict[str, Any]:
        return get_client().get_custom_emoji_list()

    @mcp.tool(
        name="owncast-internal-get-chat-messages",
        description="Gets a list of chat messages",
        tags={"internal"},
    )
    def get_chat_messages(access_token: str) -> dict[str, Any]:
        return get_client().get_chat_messages(access_token)

    @mcp.tool(
        name="owncast-internal-register-anonymous-chat-user",
        description="Registers an anonymous chat user",
        tags={"internal"},
    )
    def register_anonymous_chat_user(
        x_forwarded_user: str | None = None, display_name: str | None = None
    ) -> dict[str, Any]:
        return get_client().register_anonymous_chat_user(x_forwarded_user, display_name)

    @mcp.tool(
        name="owncast-internal-update-message-visibility",
        description="Update chat message visibility",
        tags={"internal"},
    )
    def update_message_visibility(access_token: str, body: dict) -> dict[str, Any]:
        return get_client().update_message_visibility(access_token, body)

    @mcp.tool(
        name="owncast-internal-update-user-enabled",
        description="Enable/disable a user",
        tags={"internal"},
    )
    def update_user_enabled(
        access_token: str, user_id: str | None = None, enabled: bool | None = None
    ) -> dict[str, Any]:
        return get_client().update_user_enabled(access_token, user_id, enabled)

    @mcp.tool(
        name="owncast-internal-get-web-config",
        description="Get the web config",
        tags={"internal"},
    )
    def get_web_config() -> dict[str, Any]:
        return get_client().get_web_config()

    @mcp.tool(
        name="owncast-internal-get-ypresponse",
        description="Get the YP protocol data",
        tags={"internal"},
    )
    def get_ypresponse() -> dict[str, Any]:
        return get_client().get_ypresponse()

    @mcp.tool(
        name="owncast-internal-get-all-social-platforms",
        description="Get all social platforms",
        tags={"internal"},
    )
    def get_all_social_platforms() -> dict[str, Any]:
        return get_client().get_all_social_platforms()

    @mcp.tool(
        name="owncast-internal-get-video-stream-output-variants",
        description="Get a list of video variants available",
        tags={"internal"},
    )
    def get_video_stream_output_variants() -> dict[str, Any]:
        return get_client().get_video_stream_output_variants()

    @mcp.tool(
        name="owncast-internal-ping",
        description="Tell the backend you're an active viewer",
        tags={"internal"},
    )
    def ping() -> dict[str, Any]:
        return get_client().ping()

    @mcp.tool(
        name="owncast-internal-remote-follow",
        description="Request remote follow",
        tags={"internal"},
    )
    def remote_follow(account: str | None = None) -> dict[str, Any]:
        return get_client().remote_follow(account)

    @mcp.tool(
        name="owncast-internal-get-followers",
        description="Gets the list of followers",
        tags={"internal"},
    )
    def get_followers(
        offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        return get_client().get_followers(offset, limit)

    @mcp.tool(
        name="owncast-internal-report-playback-metrics",
        description="Save video playback metrics for future video health recording",
        tags={"internal"},
    )
    def report_playback_metrics(body: dict) -> dict[str, Any]:
        return get_client().report_playback_metrics(body)

    @mcp.tool(
        name="owncast-internal-register-for-live-notifications",
        description="Register for notifications",
        tags={"internal"},
    )
    def register_for_live_notifications(
        access_token: str,
        channel: str | None = None,
        destination: str | None = None,
    ) -> dict[str, Any]:
        return get_client().register_for_live_notifications(
            access_token, channel, destination
        )

    @mcp.tool(
        name="owncast-internal-status-admin",
        description="Get current inboard broadcaster",
        tags={"internal"},
    )
    def status_admin() -> dict[str, Any]:
        return get_client().status_admin()

    @mcp.tool(
        name="owncast-internal-disconnect-inbound-connection",
        description="Disconnect inbound stream",
        tags={"internal"},
    )
    def disconnect_inbound_connection() -> dict[str, Any]:
        return get_client().disconnect_inbound_connection()

    @mcp.tool(
        name="owncast-internal-get-server-config",
        description="Get the current server config",
        tags={"internal"},
    )
    def get_server_config() -> dict[str, Any]:
        return get_client().get_server_config()

    @mcp.tool(
        name="owncast-internal-get-viewers-over-time",
        description="Get viewer count over time",
        tags={"internal"},
    )
    def get_viewers_over_time(window_start: str | None = None) -> dict[str, Any]:
        return get_client().get_viewers_over_time(window_start)

    @mcp.tool(
        name="owncast-internal-get-active-viewers",
        description="Get active viewers",
        tags={"internal"},
    )
    def get_active_viewers() -> dict[str, Any]:
        return get_client().get_active_viewers()

    @mcp.tool(
        name="owncast-internal-get-hardware-stats",
        description="Get the current hardware stats",
        tags={"internal"},
    )
    def get_hardware_stats() -> dict[str, Any]:
        return get_client().get_hardware_stats()

    @mcp.tool(
        name="owncast-internal-get-connected-chat-clients",
        description="Get a detailed list of currently connected chat clients",
        tags={"internal"},
    )
    def get_connected_chat_clients() -> dict[str, Any]:
        return get_client().get_connected_chat_clients()

    @mcp.tool(
        name="owncast-internal-get-chat-messages-admin",
        description="Get all chat messages for the admin, unfiltered",
        tags={"internal"},
    )
    def get_chat_messages_admin() -> dict[str, Any]:
        return get_client().get_chat_messages_admin()

    @mcp.tool(
        name="owncast-internal-update-message-visibility-admin",
        description="Update visibility of chat messages",
        tags={"internal"},
    )
    def update_message_visibility_admin(body: dict) -> dict[str, Any]:
        return get_client().update_message_visibility_admin(body)

    @mcp.tool(
        name="owncast-internal-update-user-enabled-admin",
        description="Enable or disable a user",
        tags={"internal"},
    )
    def update_user_enabled_admin(
        user_id: str | None = None, enabled: bool | None = None
    ) -> dict[str, Any]:
        return get_client().update_user_enabled_admin(user_id, enabled)

    @mcp.tool(
        name="owncast-internal-get-disabled-users",
        description="Get a list of disabled users",
        tags={"internal"},
    )
    def get_disabled_users() -> dict[str, Any]:
        return get_client().get_disabled_users()

    @mcp.tool(
        name="owncast-internal-ban-ipaddress",
        description="Ban an IP address",
        tags={"internal"},
    )
    def ban_ipaddress(body: dict) -> dict[str, Any]:
        return get_client().ban_ipaddress(body)

    @mcp.tool(
        name="owncast-internal-unban-ipaddress",
        description="Remove an IP ban",
        tags={"internal"},
    )
    def unban_ipaddress(body: dict) -> dict[str, Any]:
        return get_client().unban_ipaddress(body)

    @mcp.tool(
        name="owncast-internal-get-ipaddress-bans",
        description="Get all banned IP addresses",
        tags={"internal"},
    )
    def get_ipaddress_bans() -> dict[str, Any]:
        return get_client().get_ipaddress_bans()

    @mcp.tool(
        name="owncast-internal-update-user-moderator",
        description="Set moderator status for a user",
        tags={"internal"},
    )
    def update_user_moderator(
        user_id: str | None = None, is_moderator: bool | None = None
    ) -> dict[str, Any]:
        return get_client().update_user_moderator(user_id, is_moderator)

    @mcp.tool(
        name="owncast-internal-get-moderators",
        description="Get a list of moderator users",
        tags={"internal"},
    )
    def get_moderators() -> dict[str, Any]:
        return get_client().get_moderators()

    @mcp.tool(
        name="owncast-internal-get-logs", description="Get all logs", tags={"internal"}
    )
    def get_logs() -> dict[str, Any]:
        return get_client().get_logs()

    @mcp.tool(
        name="owncast-internal-get-warnings",
        description="Get warning/error logs",
        tags={"internal"},
    )
    def get_warnings() -> dict[str, Any]:
        return get_client().get_warnings()

    @mcp.tool(
        name="owncast-internal-get-followers-admin",
        description="Get followers",
        tags={"internal"},
    )
    def get_followers_admin(
        offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        return get_client().get_followers_admin(offset, limit)

    @mcp.tool(
        name="owncast-internal-get-pending-follow-requests",
        description="Get a list of pending follow requests",
        tags={"internal"},
    )
    def get_pending_follow_requests() -> dict[str, Any]:
        return get_client().get_pending_follow_requests()

    @mcp.tool(
        name="owncast-internal-get-blocked-and-rejected-followers",
        description="Get a list of rejected or blocked follows",
        tags={"internal"},
    )
    def get_blocked_and_rejected_followers() -> dict[str, Any]:
        return get_client().get_blocked_and_rejected_followers()

    @mcp.tool(
        name="owncast-internal-approve-follower",
        description="Set the following state of a follower or follow request",
        tags={"internal"},
    )
    def approve_follower(
        actor_iri: str | None = None, approved: bool | None = None
    ) -> dict[str, Any]:
        return get_client().approve_follower(actor_iri, approved)

    @mcp.tool(
        name="owncast-internal-upload-custom-emoji",
        description="Upload custom emoji",
        tags={"internal"},
    )
    def upload_custom_emoji(
        name: str | None = None, data: str | None = None
    ) -> dict[str, Any]:
        return get_client().upload_custom_emoji(name, data)

    @mcp.tool(
        name="owncast-internal-delete-custom-emoji",
        description="Delete custom emoji",
        tags={"internal"},
    )
    def delete_custom_emoji(name: str | None = None) -> dict[str, Any]:
        return get_client().delete_custom_emoji(name)

    @mcp.tool(
        name="owncast-internal-set-admin-password",
        description="Change the current admin password",
        tags={"internal"},
    )
    def set_admin_password(body: dict) -> dict[str, Any]:
        return get_client().set_admin_password(body)

    @mcp.tool(
        name="owncast-internal-set-stream-keys",
        description="Set an array of valid stream keys",
        tags={"internal"},
    )
    def set_stream_keys(value: list | None = None) -> dict[str, Any]:
        return get_client().set_stream_keys(value)

    @mcp.tool(
        name="owncast-internal-set-extra-page-content",
        description="Change the extra page content in memory",
        tags={"internal"},
    )
    def set_extra_page_content(body: dict) -> dict[str, Any]:
        return get_client().set_extra_page_content(body)

    @mcp.tool(
        name="owncast-internal-set-stream-title",
        description="Change the stream title",
        tags={"internal"},
    )
    def set_stream_title(body: dict) -> dict[str, Any]:
        return get_client().set_stream_title(body)

    @mcp.tool(
        name="owncast-internal-set-server-welcome-message",
        description="Change the welcome message",
        tags={"internal"},
    )
    def set_server_welcome_message(body: dict) -> dict[str, Any]:
        return get_client().set_server_welcome_message(body)

    @mcp.tool(
        name="owncast-internal-set-chat-disabled",
        description="Disable chat",
        tags={"internal"},
    )
    def set_chat_disabled(body: dict) -> dict[str, Any]:
        return get_client().set_chat_disabled(body)

    @mcp.tool(
        name="owncast-internal-set-chat-join-messages-enabled",
        description="Enable chat for user join messages",
        tags={"internal"},
    )
    def set_chat_join_messages_enabled(body: dict) -> dict[str, Any]:
        return get_client().set_chat_join_messages_enabled(body)

    @mcp.tool(
        name="owncast-internal-set-enable-established-chat-user-mode",
        description="Enable/disable chat established user mode",
        tags={"internal"},
    )
    def set_enable_established_chat_user_mode(body: dict) -> dict[str, Any]:
        return get_client().set_enable_established_chat_user_mode(body)

    @mcp.tool(
        name="owncast-internal-set-forbidden-username-list",
        description="Set chat usernames that are not allowed",
        tags={"internal"},
    )
    def set_forbidden_username_list(value: list | None = None) -> dict[str, Any]:
        return get_client().set_forbidden_username_list(value)

    @mcp.tool(
        name="owncast-internal-set-suggested-username-list",
        description="Set the suggested chat usernames that will be assigned automatically",
        tags={"internal"},
    )
    def set_suggested_username_list(value: list | None = None) -> dict[str, Any]:
        return get_client().set_suggested_username_list(value)

    @mcp.tool(
        name="owncast-internal-set-chat-spam-protection-enabled",
        description="Set spam protection enabled",
        tags={"internal"},
    )
    def set_chat_spam_protection_enabled(body: dict) -> dict[str, Any]:
        return get_client().set_chat_spam_protection_enabled(body)

    @mcp.tool(
        name="owncast-internal-set-chat-slur-filter-enabled",
        description="Set slur filter enabled",
        tags={"internal"},
    )
    def set_chat_slur_filter_enabled(body: dict) -> dict[str, Any]:
        return get_client().set_chat_slur_filter_enabled(body)

    @mcp.tool(
        name="owncast-internal-set-chat-require-authentication",
        description="Set require authentication for chat",
        tags={"internal"},
    )
    def set_chat_require_authentication(body: dict) -> dict[str, Any]:
        return get_client().set_chat_require_authentication(body)

    @mcp.tool(
        name="owncast-internal-set-video-codec",
        description="Set video codec",
        tags={"internal"},
    )
    def set_video_codec(body: dict) -> dict[str, Any]:
        return get_client().set_video_codec(body)

    @mcp.tool(
        name="owncast-internal-set-stream-latency-level",
        description="Set the number of video segments and duration per segment in a playlist",
        tags={"internal"},
    )
    def set_stream_latency_level(body: dict) -> dict[str, Any]:
        return get_client().set_stream_latency_level(body)

    @mcp.tool(
        name="owncast-internal-set-stream-output-variants",
        description="Set an array of video output configurations",
        tags={"internal"},
    )
    def set_stream_output_variants(value: list | None = None) -> dict[str, Any]:
        return get_client().set_stream_output_variants(value)

    @mcp.tool(
        name="owncast-internal-set-custom-color-variable-values",
        description="Set style/color/css values",
        tags={"internal"},
    )
    def set_custom_color_variable_values(
        value: dict | None = None,
    ) -> dict[str, Any]:
        return get_client().set_custom_color_variable_values(value)

    @mcp.tool(
        name="owncast-internal-set-logo", description="Update logo", tags={"internal"}
    )
    def set_logo(body: dict) -> dict[str, Any]:
        return get_client().set_logo(body)

    @mcp.tool(
        name="owncast-internal-set-favicon",
        description="Upload custom favicon",
        tags={"internal"},
    )
    def set_favicon() -> dict[str, Any]:
        return get_client().set_favicon()

    @mcp.tool(
        name="owncast-internal-reset-favicon",
        description="Reset favicon to default",
        tags={"internal"},
    )
    def reset_favicon() -> dict[str, Any]:
        return get_client().reset_favicon()

    @mcp.tool(
        name="owncast-internal-set-tags",
        description="Update server tags",
        tags={"internal"},
    )
    def set_tags(body: dict) -> dict[str, Any]:
        return get_client().set_tags(body)

    @mcp.tool(
        name="owncast-internal-set-ffmpeg-path",
        description="Update FFMPEG path",
        tags={"internal"},
    )
    def set_ffmpeg_path(body: dict) -> dict[str, Any]:
        return get_client().set_ffmpeg_path(body)

    @mcp.tool(
        name="owncast-internal-set-web-server-port",
        description="Update server port",
        tags={"internal"},
    )
    def set_web_server_port(body: dict) -> dict[str, Any]:
        return get_client().set_web_server_port(body)

    @mcp.tool(
        name="owncast-internal-set-web-server-ip",
        description="Update server IP address",
        tags={"internal"},
    )
    def set_web_server_ip(body: dict) -> dict[str, Any]:
        return get_client().set_web_server_ip(body)

    @mcp.tool(
        name="owncast-internal-set-rtmpserver-port",
        description="Update RTMP post",
        tags={"internal"},
    )
    def set_rtmpserver_port(body: dict) -> dict[str, Any]:
        return get_client().set_rtmpserver_port(body)

    @mcp.tool(
        name="owncast-internal-set-socket-host-override",
        description="Update websocket host override",
        tags={"internal"},
    )
    def set_socket_host_override(body: dict) -> dict[str, Any]:
        return get_client().set_socket_host_override(body)

    @mcp.tool(
        name="owncast-internal-set-video-serving-endpoint",
        description="Update custom video serving endpoint",
        tags={"internal"},
    )
    def set_video_serving_endpoint(body: dict) -> dict[str, Any]:
        return get_client().set_video_serving_endpoint(body)

    @mcp.tool(
        name="owncast-internal-set-nsfw",
        description="Update NSFW marking",
        tags={"internal"},
    )
    def set_nsfw(body: dict) -> dict[str, Any]:
        return get_client().set_nsfw(body)

    @mcp.tool(
        name="owncast-internal-set-directory-enabled",
        description="Update directory enabled",
        tags={"internal"},
    )
    def set_directory_enabled(body: dict) -> dict[str, Any]:
        return get_client().set_directory_enabled(body)

    @mcp.tool(
        name="owncast-internal-set-social-handles",
        description="Update social handles",
        tags={"internal"},
    )
    def set_social_handles(value: list | None = None) -> dict[str, Any]:
        return get_client().set_social_handles(value)

    @mcp.tool(
        name="owncast-internal-set-s3-configuration",
        description="Update S3 configuration",
        tags={"internal"},
    )
    def set_s3_configuration(value: Any | None = None) -> dict[str, Any]:
        return get_client().set_s3_configuration(value)

    @mcp.tool(
        name="owncast-internal-set-server-url",
        description="Update server url",
        tags={"internal"},
    )
    def set_server_url(body: dict) -> dict[str, Any]:
        return get_client().set_server_url(body)

    @mcp.tool(
        name="owncast-internal-set-external-actions",
        description="Update external action links",
        tags={"internal"},
    )
    def set_external_actions(value: list | None = None) -> dict[str, Any]:
        return get_client().set_external_actions(value)

    @mcp.tool(
        name="owncast-internal-set-custom-styles",
        description="Update custom styles",
        tags={"internal"},
    )
    def set_custom_styles(body: dict) -> dict[str, Any]:
        return get_client().set_custom_styles(body)

    @mcp.tool(
        name="owncast-internal-set-custom-javascript",
        description="Update custom JavaScript",
        tags={"internal"},
    )
    def set_custom_javascript(body: dict) -> dict[str, Any]:
        return get_client().set_custom_javascript(body)

    @mcp.tool(
        name="owncast-internal-set-hide-viewer-count",
        description="Update hide viewer count",
        tags={"internal"},
    )
    def set_hide_viewer_count(body: dict) -> dict[str, Any]:
        return get_client().set_hide_viewer_count(body)

    @mcp.tool(
        name="owncast-internal-set-disable-search-indexing",
        description="Update search indexing",
        tags={"internal"},
    )
    def set_disable_search_indexing(body: dict) -> dict[str, Any]:
        return get_client().set_disable_search_indexing(body)

    @mcp.tool(
        name="owncast-internal-set-federation-enabled",
        description="Enable/disable federation features",
        tags={"internal"},
    )
    def set_federation_enabled(body: dict) -> dict[str, Any]:
        return get_client().set_federation_enabled(body)

    @mcp.tool(
        name="owncast-internal-set-federation-activity-private",
        description="Set if federation activities are private",
        tags={"internal"},
    )
    def set_federation_activity_private(body: dict) -> dict[str, Any]:
        return get_client().set_federation_activity_private(body)

    @mcp.tool(
        name="owncast-internal-set-federation-show-engagement",
        description="Set if fediverse engagement appears in chat",
        tags={"internal"},
    )
    def set_federation_show_engagement(body: dict) -> dict[str, Any]:
        return get_client().set_federation_show_engagement(body)

    @mcp.tool(
        name="owncast-internal-set-federation-username",
        description="Set local federated username",
        tags={"internal"},
    )
    def set_federation_username(body: dict) -> dict[str, Any]:
        return get_client().set_federation_username(body)

    @mcp.tool(
        name="owncast-internal-set-federation-go-live-message",
        description="Set federated go live message",
        tags={"internal"},
    )
    def set_federation_go_live_message(body: dict) -> dict[str, Any]:
        return get_client().set_federation_go_live_message(body)

    @mcp.tool(
        name="owncast-internal-set-federation-block-domains",
        description="Set Federation blocked domains",
        tags={"internal"},
    )
    def set_federation_block_domains(body: dict) -> dict[str, Any]:
        return get_client().set_federation_block_domains(body)

    @mcp.tool(
        name="owncast-internal-set-discord-notification-configuration",
        description="Configure Discord notifications",
        tags={"internal"},
    )
    def set_discord_notification_configuration(
        value: Any | None = None,
    ) -> dict[str, Any]:
        return get_client().set_discord_notification_configuration(value)

    @mcp.tool(
        name="owncast-internal-set-browser-notification-configuration",
        description="Configure Browser notifications",
        tags={"internal"},
    )
    def set_browser_notification_configuration(
        value: Any | None = None,
    ) -> dict[str, Any]:
        return get_client().set_browser_notification_configuration(value)

    @mcp.tool(
        name="owncast-internal-get-webhooks",
        description="Get all the webhooks",
        tags={"internal"},
    )
    def get_webhooks() -> dict[str, Any]:
        return get_client().get_webhooks()

    @mcp.tool(
        name="owncast-internal-delete-webhook",
        description="Delete a single webhook",
        tags={"internal"},
    )
    def delete_webhook(id: int | None = None) -> dict[str, Any]:
        return get_client().delete_webhook(id)

    @mcp.tool(
        name="owncast-internal-create-webhook",
        description="Create a single webhook",
        tags={"internal"},
    )
    def create_webhook(
        url: str | None = None, events: list | None = None
    ) -> dict[str, Any]:
        return get_client().create_webhook(url, events)

    @mcp.tool(
        name="owncast-internal-get-external-apiusers",
        description="Get all access tokens",
        tags={"internal"},
    )
    def get_external_apiusers() -> dict[str, Any]:
        return get_client().get_external_apiusers()

    @mcp.tool(
        name="owncast-internal-delete-external-apiuser",
        description="Delete a single external API user",
        tags={"internal"},
    )
    def delete_external_apiuser(token: str | None = None) -> dict[str, Any]:
        return get_client().delete_external_apiuser(token)

    @mcp.tool(
        name="owncast-internal-create-external-apiuser",
        description="Create a single access token",
        tags={"internal"},
    )
    def create_external_apiuser(
        name: str | None = None, scopes: list | None = None
    ) -> dict[str, Any]:
        return get_client().create_external_apiuser(name, scopes)

    @mcp.tool(
        name="owncast-internal-auto-update-options",
        description="Return the auto-update features that are supported for this instance",
        tags={"internal"},
    )
    def auto_update_options() -> dict[str, Any]:
        return get_client().auto_update_options()

    @mcp.tool(
        name="owncast-internal-auto-update-start",
        description="Begin the auto-update",
        tags={"internal"},
    )
    def auto_update_start() -> dict[str, Any]:
        return get_client().auto_update_start()

    @mcp.tool(
        name="owncast-internal-auto-update-force-quit",
        description="Force quit the server and restart it",
        tags={"internal"},
    )
    def auto_update_force_quit() -> dict[str, Any]:
        return get_client().auto_update_force_quit()

    @mcp.tool(
        name="owncast-internal-reset-ypregistration",
        description="Reset YP configuration",
        tags={"internal"},
    )
    def reset_ypregistration() -> dict[str, Any]:
        return get_client().reset_ypregistration()

    @mcp.tool(
        name="owncast-internal-get-video-playback-metrics",
        description="Get video playback metrics",
        tags={"internal"},
    )
    def get_video_playback_metrics() -> dict[str, Any]:
        return get_client().get_video_playback_metrics()

    @mcp.tool(
        name="owncast-internal-get-prometheus-api",
        description="Endpoint to interface with Prometheus",
        tags={"internal"},
    )
    def get_prometheus_api() -> dict[str, Any]:
        return get_client().get_prometheus_api()

    @mcp.tool(
        name="owncast-internal-post-prometheus-api",
        description="Endpoint to interface with Prometheus",
        tags={"internal"},
    )
    def post_prometheus_api() -> dict[str, Any]:
        return get_client().post_prometheus_api()

    @mcp.tool(
        name="owncast-internal-put-prometheus-api",
        description="Endpoint to interface with Prometheus",
        tags={"internal"},
    )
    def put_prometheus_api() -> dict[str, Any]:
        return get_client().put_prometheus_api()

    @mcp.tool(
        name="owncast-internal-delete-prometheus-api",
        description="Endpoint to interface with Prometheus",
        tags={"internal"},
    )
    def delete_prometheus_api() -> dict[str, Any]:
        return get_client().delete_prometheus_api()

    @mcp.tool(
        name="owncast-internal-send-federated-message",
        description="Send a public message to the Fediverse from the server's user",
        tags={"internal"},
    )
    def send_federated_message(body: dict) -> dict[str, Any]:
        return get_client().send_federated_message(body)

    @mcp.tool(
        name="owncast-internal-get-federated-actions",
        description="Get a paginated list of federated activities",
        tags={"internal"},
    )
    def get_federated_actions(
        offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        return get_client().get_federated_actions(offset, limit)

    @mcp.tool(
        name="owncast-internal-start-indie-auth-flow",
        description="Begins auth flow",
        tags={"internal"},
    )
    def start_indie_auth_flow(
        access_token: str, auth_host: str | None = None
    ) -> dict[str, Any]:
        return get_client().start_indie_auth_flow(access_token, auth_host)

    @mcp.tool(
        name="owncast-internal-handle-indie-auth-redirect",
        description="Handle the redirect from an IndieAuth server to continue the auth flow",
        tags={"internal"},
    )
    def handle_indie_auth_redirect(state: str) -> dict[str, Any]:
        return get_client().handle_indie_auth_redirect(state)

    @mcp.tool(
        name="owncast-internal-handle-indie-auth-endpoint-get",
        description="Handles the IndieAuth auth endpoint",
        tags={"internal"},
    )
    def handle_indie_auth_endpoint_get(
        client_id: str, redirect_uri: str, code_challenge: str, state: str
    ) -> dict[str, Any]:
        return get_client().handle_indie_auth_endpoint_get(
            client_id, redirect_uri, code_challenge, state
        )

    @mcp.tool(
        name="owncast-internal-handle-indie-auth-endpoint-post",
        description="Handles IndieAuth from form submission",
        tags={"internal"},
    )
    def handle_indie_auth_endpoint_post() -> dict[str, Any]:
        return get_client().handle_indie_auth_endpoint_post()

    @mcp.tool(
        name="owncast-internal-register-fediverse-otprequest",
        description="Register a Fediverse OTP request",
        tags={"internal"},
    )
    def register_fediverse_otprequest(
        access_token: str, account: str | None = None
    ) -> dict[str, Any]:
        return get_client().register_fediverse_otprequest(access_token, account)

    @mcp.tool(
        name="owncast-internal-verify-fediverse-otprequest",
        description="Verify Fediverse OTP code",
        tags={"internal"},
    )
    def verify_fediverse_otprequest(code: str | None = None) -> dict[str, Any]:
        return get_client().verify_fediverse_otprequest(code)


def register_objects_tools(mcp: FastMCP):
    @mcp.tool(
        name="owncast-objects-set-server-name",
        description="Change the server name",
        tags={"objects"},
    )
    def set_server_name(body: dict) -> dict[str, Any]:
        return get_client().set_server_name(body)

    @mcp.tool(
        name="owncast-objects-set-server-summary",
        description="Change the server summary",
        tags={"objects"},
    )
    def set_server_summary(body: dict) -> dict[str, Any]:
        return get_client().set_server_summary(body)

    @mcp.tool(
        name="owncast-objects-set-custom-offline-message",
        description="Change the offline message",
        tags={"objects"},
    )
    def set_custom_offline_message(body: dict) -> dict[str, Any]:
        return get_client().set_custom_offline_message(body)


def register_external_tools(mcp: FastMCP):
    @mcp.tool(
        name="owncast-external-send-system-message",
        description="Send a system message to the chat",
        tags={"external"},
    )
    def send_system_message(body: dict) -> dict[str, Any]:
        return get_client().send_system_message(body)

    @mcp.tool(
        name="owncast-external-send-system-message-to-connected-client",
        description="Send a system message to a single client",
        tags={"external"},
    )
    def send_system_message_to_connected_client(
        client_id: int, body: dict
    ) -> dict[str, Any]:
        return get_client().send_system_message_to_connected_client(client_id, body)

    @mcp.tool(
        name="owncast-external-send-user-message",
        description="Send a user message to chat",
        tags={"external"},
    )
    def send_user_message() -> dict[str, Any]:
        return get_client().send_user_message()

    @mcp.tool(
        name="owncast-external-send-integration-chat-message",
        description="Send a message to chat as a specific 3rd party bot/integration based on its access token",
        tags={"external"},
    )
    def send_integration_chat_message(body: dict) -> dict[str, Any]:
        return get_client().send_integration_chat_message(body)

    @mcp.tool(
        name="owncast-external-send-chat-action",
        description="Send a user action to chat",
        tags={"external"},
    )
    def send_chat_action(body: dict) -> dict[str, Any]:
        return get_client().send_chat_action(body)

    @mcp.tool(
        name="owncast-external-update-message-visibility",
        description="Hide chat message",
        tags={"external"},
    )
    def external_update_message_visibility(body: dict) -> dict[str, Any]:
        return get_client().external_update_message_visibility(body)

    @mcp.tool(
        name="owncast-external-get-status",
        description="Get the server's status",
        tags={"external"},
    )
    def external_get_status() -> dict[str, Any]:
        return get_client().external_get_status()

    @mcp.tool(
        name="owncast-external-set-stream-title",
        description="Stream title",
        tags={"external"},
    )
    def external_set_stream_title(body: dict) -> dict[str, Any]:
        return get_client().external_set_stream_title(body)

    @mcp.tool(
        name="owncast-external-get-chat-messages",
        description="Get chat history",
        tags={"external"},
    )
    def external_get_chat_messages() -> dict[str, Any]:
        return get_client().external_get_chat_messages()

    @mcp.tool(
        name="owncast-external-get-connected-chat-clients",
        description="Connected clients",
        tags={"external"},
    )
    def external_get_connected_chat_clients() -> dict[str, Any]:
        return get_client().external_get_connected_chat_clients()

    @mcp.tool(
        name="owncast-external-get-user-details",
        description="Get a user's details",
        tags={"external"},
    )
    def external_get_user_details(user_id: str) -> dict[str, Any]:
        return get_client().external_get_user_details(user_id)


def register_chat_tools(mcp: FastMCP):
    @mcp.tool(
        name="owncast-chat-get-user-details",
        description="Get a user's details",
        tags={"chat"},
    )
    def get_user_details(user_id: str, access_token: str) -> dict[str, Any]:
        return get_client().get_user_details(user_id, access_token)


def register_all_tools(mcp: FastMCP) -> list[str]:
    registered_tags = []
    if to_boolean(os.getenv("CHAT_TOOL", "True")):
        register_chat_tools(mcp)
        registered_tags.append("chat")
    if to_boolean(os.getenv("EXTERNAL_TOOL", "True")):
        register_external_tools(mcp)
        registered_tags.append("external")
    if to_boolean(os.getenv("INTERNAL_TOOL", "True")):
        register_internal_tools(mcp)
        registered_tags.append("internal")
    if to_boolean(os.getenv("OBJECTS_TOOL", "True")):
        register_objects_tools(mcp)
        registered_tags.append("objects")
    return registered_tags


### END GENERATED TOOL REGISTRATION ###


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    load_dotenv(find_dotenv())

    args, mcp, middlewares = create_mcp_server(
        name="owncast",
        version=__version__,
        instructions="Owncast Agent MCP Server",
    )

    registered_tags = register_all_tools(mcp)
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
