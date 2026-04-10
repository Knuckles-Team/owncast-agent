from typing import Dict, Any, Optional
import requests
from agent_utilities.exceptions import AuthError, ApiError


class OwncastApi:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=data,
                params=params,
            )
            if response.status_code == 401:
                raise AuthError(f"Unauthorized: {response.text}")
            response.raise_for_status()
            if response.text:
                try:
                    return response.json()
                except Exception:
                    return {"status": "success", "text": response.text}
            return {"success": True}
        except requests.exceptions.RequestException as e:
            raise ApiError(f"API request failed: {e}")

    def get_status(
        self,
    ) -> Dict[str, Any]:
        """Get the status of the server"""
        return self._request("GET", "/status", params=None, data=None)

    def get_custom_emoji_list(
        self,
    ) -> Dict[str, Any]:
        """Get list of custom emojis supported in the chat"""
        return self._request("GET", "/emoji", params=None, data=None)

    def get_chat_messages(self, access_token: str) -> Dict[str, Any]:
        """Gets a list of chat messages"""
        return self._request(
            "GET", "/chat", params={"accessToken": access_token}, data=None
        )

    def register_anonymous_chat_user(
        self, x_forwarded_user: Optional[str] = None, display_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Registers an anonymous chat user"""
        return self._request(
            "POST",
            "/chat/register",
            params={"X-Forwarded-User": x_forwarded_user},
            data={"displayName": display_name},
        )

    def update_message_visibility(
        self, access_token: str, body: dict
    ) -> Dict[str, Any]:
        """Update chat message visibility"""
        return self._request(
            "POST",
            "/chat/messagevisibility",
            params={"accessToken": access_token},
            data=body,
        )

    def update_user_enabled(
        self,
        access_token: str,
        user_id: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Enable/disable a user"""
        return self._request(
            "POST",
            "/chat/users/setenabled",
            params={"accessToken": access_token},
            data={"userId": user_id, "enabled": enabled},
        )

    def get_web_config(
        self,
    ) -> Dict[str, Any]:
        """Get the web config"""
        return self._request("GET", "/config", params=None, data=None)

    def get_ypresponse(
        self,
    ) -> Dict[str, Any]:
        """Get the YP protocol data"""
        return self._request("GET", "/yp", params=None, data=None)

    def get_all_social_platforms(
        self,
    ) -> Dict[str, Any]:
        """Get all social platforms"""
        return self._request("GET", "/socialplatforms", params=None, data=None)

    def get_video_stream_output_variants(
        self,
    ) -> Dict[str, Any]:
        """Get a list of video variants available"""
        return self._request("GET", "/video/variants", params=None, data=None)

    def ping(
        self,
    ) -> Dict[str, Any]:
        """Tell the backend you're an active viewer"""
        return self._request("GET", "/ping", params=None, data=None)

    def remote_follow(self, account: Optional[str] = None) -> Dict[str, Any]:
        """Request remote follow"""
        return self._request(
            "POST", "/remotefollow", params=None, data={"account": account}
        )

    def get_followers(
        self, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets the list of followers"""
        return self._request(
            "GET", "/followers", params={"offset": offset, "limit": limit}, data=None
        )

    def report_playback_metrics(self, body: dict) -> Dict[str, Any]:
        """Save video playback metrics for future video health recording"""
        return self._request("POST", "/metrics/playback", params=None, data=body)

    def register_for_live_notifications(
        self,
        access_token: str,
        channel: Optional[str] = None,
        destination: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Register for notifications"""
        return self._request(
            "POST",
            "/notifications/register",
            params={"accessToken": access_token},
            data={"channel": channel, "destination": destination},
        )

    def status_admin(
        self,
    ) -> Dict[str, Any]:
        """Get current inboard broadcaster"""
        return self._request("GET", "/admin/status", params=None, data=None)

    def disconnect_inbound_connection(
        self,
    ) -> Dict[str, Any]:
        """Disconnect inbound stream"""
        return self._request("GET", "/admin/disconnect", params=None, data=None)

    def get_server_config(
        self,
    ) -> Dict[str, Any]:
        """Get the current server config"""
        return self._request("GET", "/admin/serverconfig", params=None, data=None)

    def get_viewers_over_time(
        self, window_start: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get viewer count over time"""
        return self._request(
            "GET",
            "/admin/viewersOverTime",
            params={"windowStart": window_start},
            data=None,
        )

    def get_active_viewers(
        self,
    ) -> Dict[str, Any]:
        """Get active viewers"""
        return self._request("GET", "/admin/viewers", params=None, data=None)

    def get_hardware_stats(
        self,
    ) -> Dict[str, Any]:
        """Get the current hardware stats"""
        return self._request("GET", "/admin/hardwarestats", params=None, data=None)

    def get_connected_chat_clients(
        self,
    ) -> Dict[str, Any]:
        """Get a detailed list of currently connected chat clients"""
        return self._request("GET", "/admin/chat/clients", params=None, data=None)

    def get_chat_messages_admin(
        self,
    ) -> Dict[str, Any]:
        """Get all chat messages for the admin, unfiltered"""
        return self._request("GET", "/admin/chat/messages", params=None, data=None)

    def update_message_visibility_admin(self, body: dict) -> Dict[str, Any]:
        """Update visibility of chat messages"""
        return self._request(
            "POST", "/admin/chat/messagevisibility", params=None, data=body
        )

    def update_user_enabled_admin(
        self, user_id: Optional[str] = None, enabled: Optional[bool] = None
    ) -> Dict[str, Any]:
        """Enable or disable a user"""
        return self._request(
            "POST",
            "/admin/chat/users/setenabled",
            params=None,
            data={"userId": user_id, "enabled": enabled},
        )

    def get_disabled_users(
        self,
    ) -> Dict[str, Any]:
        """Get a list of disabled users"""
        return self._request(
            "GET", "/admin/chat/users/disabled", params=None, data=None
        )

    def ban_ipaddress(self, body: dict) -> Dict[str, Any]:
        """Ban an IP address"""
        return self._request(
            "POST", "/admin/chat/users/ipbans/create", params=None, data=body
        )

    def unban_ipaddress(self, body: dict) -> Dict[str, Any]:
        """Remove an IP ban"""
        return self._request(
            "POST", "/admin/chat/users/ipbans/remove", params=None, data=body
        )

    def get_ipaddress_bans(
        self,
    ) -> Dict[str, Any]:
        """Get all banned IP addresses"""
        return self._request("GET", "/admin/chat/users/ipbans", params=None, data=None)

    def update_user_moderator(
        self, user_id: Optional[str] = None, is_moderator: Optional[bool] = None
    ) -> Dict[str, Any]:
        """Set moderator status for a user"""
        return self._request(
            "POST",
            "/admin/chat/users/setmoderator",
            params=None,
            data={"userId": user_id, "isModerator": is_moderator},
        )

    def get_moderators(
        self,
    ) -> Dict[str, Any]:
        """Get a list of moderator users"""
        return self._request(
            "GET", "/admin/chat/users/moderators", params=None, data=None
        )

    def get_logs(
        self,
    ) -> Dict[str, Any]:
        """Get all logs"""
        return self._request("GET", "/admin/logs", params=None, data=None)

    def get_warnings(
        self,
    ) -> Dict[str, Any]:
        """Get warning/error logs"""
        return self._request("GET", "/admin/logs/warnings", params=None, data=None)

    def get_followers_admin(
        self, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        """Get followers"""
        return self._request(
            "GET",
            "/admin/followers",
            params={"offset": offset, "limit": limit},
            data=None,
        )

    def get_pending_follow_requests(
        self,
    ) -> Dict[str, Any]:
        """Get a list of pending follow requests"""
        return self._request("GET", "/admin/followers/pending", params=None, data=None)

    def get_blocked_and_rejected_followers(
        self,
    ) -> Dict[str, Any]:
        """Get a list of rejected or blocked follows"""
        return self._request("GET", "/admin/followers/blocked", params=None, data=None)

    def approve_follower(
        self, actor_iri: Optional[str] = None, approved: Optional[bool] = None
    ) -> Dict[str, Any]:
        """Set the following state of a follower or follow request"""
        return self._request(
            "POST",
            "/admin/followers/approve",
            params=None,
            data={"actorIRI": actor_iri, "approved": approved},
        )

    def upload_custom_emoji(
        self, name: Optional[str] = None, data: Optional[str] = None
    ) -> Dict[str, Any]:
        """Upload custom emoji"""
        return self._request(
            "POST",
            "/admin/emoji/upload",
            params=None,
            data={"name": name, "data": data},
        )

    def delete_custom_emoji(self, name: Optional[str] = None) -> Dict[str, Any]:
        """Delete custom emoji"""
        return self._request(
            "POST", "/admin/emoji/delete", params=None, data={"name": name}
        )

    def set_admin_password(self, body: dict) -> Dict[str, Any]:
        """Change the current admin password"""
        return self._request("POST", "/admin/config/adminpass", params=None, data=body)

    def set_stream_keys(self, value: Optional[list] = None) -> Dict[str, Any]:
        """Set an array of valid stream keys"""
        return self._request(
            "POST", "/admin/config/streamkeys", params=None, data={"value": value}
        )

    def set_extra_page_content(self, body: dict) -> Dict[str, Any]:
        """Change the extra page content in memory"""
        return self._request(
            "POST", "/admin/config/pagecontent", params=None, data=body
        )

    def set_stream_title(self, body: dict) -> Dict[str, Any]:
        """Change the stream title"""
        return self._request(
            "POST", "/admin/config/streamtitle", params=None, data=body
        )

    def set_server_name(self, body: dict) -> Dict[str, Any]:
        """Change the server name"""
        return self._request("POST", "/admin/config/name", params=None, data=body)

    def set_server_summary(self, body: dict) -> Dict[str, Any]:
        """Change the server summary"""
        return self._request(
            "POST", "/admin/config/serversummary", params=None, data=body
        )

    def set_custom_offline_message(self, body: dict) -> Dict[str, Any]:
        """Change the offline message"""
        return self._request(
            "POST", "/admin/config/offlinemessage", params=None, data=body
        )

    def set_server_welcome_message(self, body: dict) -> Dict[str, Any]:
        """Change the welcome message"""
        return self._request(
            "POST", "/admin/config/welcomemessage", params=None, data=body
        )

    def set_chat_disabled(self, body: dict) -> Dict[str, Any]:
        """Disable chat"""
        return self._request(
            "POST", "/admin/config/chat/disable", params=None, data=body
        )

    def set_chat_join_messages_enabled(self, body: dict) -> Dict[str, Any]:
        """Enable chat for user join messages"""
        return self._request(
            "POST", "/admin/config/chat/joinmessagesenabled", params=None, data=body
        )

    def set_enable_established_chat_user_mode(self, body: dict) -> Dict[str, Any]:
        """Enable/disable chat established user mode"""
        return self._request(
            "POST", "/admin/config/chat/establishedusermode", params=None, data=body
        )

    def set_forbidden_username_list(
        self, value: Optional[list] = None
    ) -> Dict[str, Any]:
        """Set chat usernames that are not allowed"""
        return self._request(
            "POST",
            "/admin/config/chat/forbiddenusernames",
            params=None,
            data={"value": value},
        )

    def set_suggested_username_list(
        self, value: Optional[list] = None
    ) -> Dict[str, Any]:
        """Set the suggested chat usernames that will be assigned automatically"""
        return self._request(
            "POST",
            "/admin/config/chat/suggestedusernames",
            params=None,
            data={"value": value},
        )

    def set_chat_spam_protection_enabled(self, body: dict) -> Dict[str, Any]:
        """Set spam protection enabled"""
        return self._request(
            "POST", "/admin/config/chat/spamprotectionenabled", params=None, data=body
        )

    def set_chat_slur_filter_enabled(self, body: dict) -> Dict[str, Any]:
        """Set slur filter enabled"""
        return self._request(
            "POST", "/admin/config/chat/slurfilterenabled", params=None, data=body
        )

    def set_chat_require_authentication(self, body: dict) -> Dict[str, Any]:
        """Set require authentication for chat"""
        return self._request(
            "POST", "/admin/config/chat/requireauthentication", params=None, data=body
        )

    def set_video_codec(self, body: dict) -> Dict[str, Any]:
        """Set video codec"""
        return self._request(
            "POST", "/admin/config/video/codec", params=None, data=body
        )

    def set_stream_latency_level(self, body: dict) -> Dict[str, Any]:
        """Set the number of video segments and duration per segment in a playlist"""
        return self._request(
            "POST", "/admin/config/video/streamlatencylevel", params=None, data=body
        )

    def set_stream_output_variants(
        self, value: Optional[list] = None
    ) -> Dict[str, Any]:
        """Set an array of video output configurations"""
        return self._request(
            "POST",
            "/admin/config/video/streamoutputvariants",
            params=None,
            data={"value": value},
        )

    def set_custom_color_variable_values(
        self, value: Optional[dict] = None
    ) -> Dict[str, Any]:
        """Set style/color/css values"""
        return self._request(
            "POST", "/admin/config/appearance", params=None, data={"value": value}
        )

    def set_logo(self, body: dict) -> Dict[str, Any]:
        """Update logo"""
        return self._request("POST", "/admin/config/logo", params=None, data=body)

    def set_favicon(
        self,
    ) -> Dict[str, Any]:
        """Upload custom favicon"""
        return self._request("POST", "/admin/config/favicon", params=None, data=None)

    def reset_favicon(
        self,
    ) -> Dict[str, Any]:
        """Reset favicon to default"""
        return self._request("DELETE", "/admin/config/favicon", params=None, data=None)

    def set_tags(self, body: dict) -> Dict[str, Any]:
        """Update server tags"""
        return self._request("POST", "/admin/config/tags", params=None, data=body)

    def set_ffmpeg_path(self, body: dict) -> Dict[str, Any]:
        """Update FFMPEG path"""
        return self._request("POST", "/admin/config/ffmpegpath", params=None, data=body)

    def set_web_server_port(self, body: dict) -> Dict[str, Any]:
        """Update server port"""
        return self._request(
            "POST", "/admin/config/webserverport", params=None, data=body
        )

    def set_web_server_ip(self, body: dict) -> Dict[str, Any]:
        """Update server IP address"""
        return self._request(
            "POST", "/admin/config/webserverip", params=None, data=body
        )

    def set_rtmpserver_port(self, body: dict) -> Dict[str, Any]:
        """Update RTMP post"""
        return self._request(
            "POST", "/admin/config/rtmpserverport", params=None, data=body
        )

    def set_socket_host_override(self, body: dict) -> Dict[str, Any]:
        """Update websocket host override"""
        return self._request(
            "POST", "/admin/config/sockethostoverride", params=None, data=body
        )

    def set_video_serving_endpoint(self, body: dict) -> Dict[str, Any]:
        """Update custom video serving endpoint"""
        return self._request(
            "POST", "/admin/config/videoservingendpoint", params=None, data=body
        )

    def set_nsfw(self, body: dict) -> Dict[str, Any]:
        """Update NSFW marking"""
        return self._request("POST", "/admin/config/nsfw", params=None, data=body)

    def set_directory_enabled(self, body: dict) -> Dict[str, Any]:
        """Update directory enabled"""
        return self._request(
            "POST", "/admin/config/directoryenabled", params=None, data=body
        )

    def set_social_handles(self, value: Optional[list] = None) -> Dict[str, Any]:
        """Update social handles"""
        return self._request(
            "POST", "/admin/config/socialhandles", params=None, data={"value": value}
        )

    def set_s3_configuration(self, value: Optional[Any] = None) -> Dict[str, Any]:
        """Update S3 configuration"""
        return self._request(
            "POST", "/admin/config/s3", params=None, data={"value": value}
        )

    def set_server_url(self, body: dict) -> Dict[str, Any]:
        """Update server url"""
        return self._request("POST", "/admin/config/serverurl", params=None, data=body)

    def set_external_actions(self, value: Optional[list] = None) -> Dict[str, Any]:
        """Update external action links"""
        return self._request(
            "POST", "/admin/config/externalactions", params=None, data={"value": value}
        )

    def set_custom_styles(self, body: dict) -> Dict[str, Any]:
        """Update custom styles"""
        return self._request(
            "POST", "/admin/config/customstyles", params=None, data=body
        )

    def set_custom_javascript(self, body: dict) -> Dict[str, Any]:
        """Update custom JavaScript"""
        return self._request(
            "POST", "/admin/config/customjavascript", params=None, data=body
        )

    def set_hide_viewer_count(self, body: dict) -> Dict[str, Any]:
        """Update hide viewer count"""
        return self._request(
            "POST", "/admin/config/hideviewercount", params=None, data=body
        )

    def set_disable_search_indexing(self, body: dict) -> Dict[str, Any]:
        """Update search indexing"""
        return self._request(
            "POST", "/admin/config/disablesearchindexing", params=None, data=body
        )

    def set_federation_enabled(self, body: dict) -> Dict[str, Any]:
        """Enable/disable federation features"""
        return self._request(
            "POST", "/admin/config/federation/enable", params=None, data=body
        )

    def set_federation_activity_private(self, body: dict) -> Dict[str, Any]:
        """Set if federation activities are private"""
        return self._request(
            "POST", "/admin/config/federation/private", params=None, data=body
        )

    def set_federation_show_engagement(self, body: dict) -> Dict[str, Any]:
        """Set if fediverse engagement appears in chat"""
        return self._request(
            "POST", "/admin/config/federation/showengagement", params=None, data=body
        )

    def set_federation_username(self, body: dict) -> Dict[str, Any]:
        """Set local federated username"""
        return self._request(
            "POST", "/admin/config/federation/username", params=None, data=body
        )

    def set_federation_go_live_message(self, body: dict) -> Dict[str, Any]:
        """Set federated go live message"""
        return self._request(
            "POST", "/admin/config/federation/livemessage", params=None, data=body
        )

    def set_federation_block_domains(self, body: dict) -> Dict[str, Any]:
        """Set Federation blocked domains"""
        return self._request(
            "POST", "/admin/config/federation/blockdomains", params=None, data=body
        )

    def set_discord_notification_configuration(
        self, value: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Configure Discord notifications"""
        return self._request(
            "POST",
            "/admin/config/notifications/discord",
            params=None,
            data={"value": value},
        )

    def set_browser_notification_configuration(
        self, value: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Configure Browser notifications"""
        return self._request(
            "POST",
            "/admin/config/notifications/browser",
            params=None,
            data={"value": value},
        )

    def get_webhooks(
        self,
    ) -> Dict[str, Any]:
        """Get all the webhooks"""
        return self._request("GET", "/admin/webhooks", params=None, data=None)

    def delete_webhook(self, id: Optional[int] = None) -> Dict[str, Any]:
        """Delete a single webhook"""
        return self._request(
            "POST", "/admin/webhooks/delete", params=None, data={"id": id}
        )

    def create_webhook(
        self, url: Optional[str] = None, events: Optional[list] = None
    ) -> Dict[str, Any]:
        """Create a single webhook"""
        return self._request(
            "POST",
            "/admin/webhooks/create",
            params=None,
            data={"url": url, "events": events},
        )

    def get_external_apiusers(
        self,
    ) -> Dict[str, Any]:
        """Get all access tokens"""
        return self._request("GET", "/admin/accesstokens", params=None, data=None)

    def delete_external_apiuser(self, token: Optional[str] = None) -> Dict[str, Any]:
        """Delete a single external API user"""
        return self._request(
            "POST", "/admin/accesstokens/delete", params=None, data={"token": token}
        )

    def create_external_apiuser(
        self, name: Optional[str] = None, scopes: Optional[list] = None
    ) -> Dict[str, Any]:
        """Create a single access token"""
        return self._request(
            "POST",
            "/admin/accesstokens/create",
            params=None,
            data={"name": name, "scopes": scopes},
        )

    def auto_update_options(
        self,
    ) -> Dict[str, Any]:
        """Return the auto-update features that are supported for this instance"""
        return self._request("GET", "/admin/update/options", params=None, data=None)

    def auto_update_start(
        self,
    ) -> Dict[str, Any]:
        """Begin the auto-update"""
        return self._request("GET", "/admin/update/start", params=None, data=None)

    def auto_update_force_quit(
        self,
    ) -> Dict[str, Any]:
        """Force quit the server and restart it"""
        return self._request("GET", "/admin/update/forcequit", params=None, data=None)

    def reset_ypregistration(
        self,
    ) -> Dict[str, Any]:
        """Reset YP configuration"""
        return self._request("GET", "/admin/yp/reset", params=None, data=None)

    def get_video_playback_metrics(
        self,
    ) -> Dict[str, Any]:
        """Get video playback metrics"""
        return self._request("GET", "/admin/metrics/video", params=None, data=None)

    def get_prometheus_api(
        self,
    ) -> Dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("GET", "/admin/prometheus", params=None, data=None)

    def post_prometheus_api(
        self,
    ) -> Dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("POST", "/admin/prometheus", params=None, data=None)

    def put_prometheus_api(
        self,
    ) -> Dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("PUT", "/admin/prometheus", params=None, data=None)

    def delete_prometheus_api(
        self,
    ) -> Dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("DELETE", "/admin/prometheus", params=None, data=None)

    def send_federated_message(self, body: dict) -> Dict[str, Any]:
        """Send a public message to the Fediverse from the server's user"""
        return self._request("POST", "/admin/federation/send", params=None, data=body)

    def get_federated_actions(
        self, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        """Get a paginated list of federated activities"""
        return self._request(
            "GET",
            "/admin/federation/actions",
            params={"offset": offset, "limit": limit},
            data=None,
        )

    def send_system_message(self, body: dict) -> Dict[str, Any]:
        """Send a system message to the chat"""
        return self._request(
            "POST", "/integrations/chat/system", params=None, data=body
        )

    def send_system_message_to_connected_client(
        self, client_id: int, body: dict
    ) -> Dict[str, Any]:
        """Send a system message to a single client"""
        return self._request(
            "POST",
            f"/integrations/chat/system/client/{client_id}",
            params=None,
            data=body,
        )

    def send_user_message(
        self,
    ) -> Dict[str, Any]:
        """Send a user message to chat"""
        return self._request("POST", "/integrations/chat/user", params=None, data=None)

    def send_integration_chat_message(self, body: dict) -> Dict[str, Any]:
        """Send a message to chat as a specific 3rd party bot/integration based on its access token"""
        return self._request("POST", "/integrations/chat/send", params=None, data=body)

    def send_chat_action(self, body: dict) -> Dict[str, Any]:
        """Send a user action to chat"""
        return self._request(
            "POST", "/integrations/chat/action", params=None, data=body
        )

    def external_update_message_visibility(self, body: dict) -> Dict[str, Any]:
        """Hide chat message"""
        return self._request(
            "POST", "/integrations/chat/messagevisibility", params=None, data=body
        )

    def external_get_status(
        self,
    ) -> Dict[str, Any]:
        """Get the server's status"""
        return self._request("GET", "/integrations/status", params=None, data=None)

    def external_set_stream_title(self, body: dict) -> Dict[str, Any]:
        """Stream title"""
        return self._request(
            "POST", "/integrations/streamtitle", params=None, data=body
        )

    def external_get_chat_messages(
        self,
    ) -> Dict[str, Any]:
        """Get chat history"""
        return self._request("GET", "/integrations/chat", params=None, data=None)

    def external_get_connected_chat_clients(
        self,
    ) -> Dict[str, Any]:
        """Connected clients"""
        return self._request("GET", "/integrations/clients", params=None, data=None)

    def external_get_user_details(self, user_id: str) -> Dict[str, Any]:
        """Get a user's details"""
        return self._request(
            "GET",
            f"/integrations/moderation/chat/user/{user_id}",
            params=None,
            data=None,
        )

    def get_user_details(self, user_id: str, access_token: str) -> Dict[str, Any]:
        """Get a user's details"""
        return self._request(
            "GET",
            f"/moderation/chat/user/{user_id}",
            params={"accessToken": access_token},
            data=None,
        )

    def start_indie_auth_flow(
        self, access_token: str, auth_host: Optional[str] = None
    ) -> Dict[str, Any]:
        """Begins auth flow"""
        return self._request(
            "POST",
            "/auth/indieauth",
            params={"accessToken": access_token},
            data={"authHost": auth_host},
        )

    def handle_indie_auth_redirect(self, state: str) -> Dict[str, Any]:
        """Handle the redirect from an IndieAuth server to continue the auth flow"""
        return self._request(
            "GET", "/auth/indieauth/callback", params={"state": state}, data=None
        )

    def handle_indie_auth_endpoint_get(
        self, client_id: str, redirect_uri: str, code_challenge: str, state: str
    ) -> Dict[str, Any]:
        """Handles the IndieAuth auth endpoint"""
        return self._request(
            "GET",
            "/auth/provider/indieauth",
            params={
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "code_challenge": code_challenge,
                "state": state,
            },
            data=None,
        )

    def handle_indie_auth_endpoint_post(
        self,
    ) -> Dict[str, Any]:
        """Handles IndieAuth from form submission"""
        return self._request("POST", "/auth/provider/indieauth", params=None, data=None)

    def register_fediverse_otprequest(
        self, access_token: str, account: Optional[str] = None
    ) -> Dict[str, Any]:
        """Register a Fediverse OTP request"""
        return self._request(
            "POST",
            "/auth/fediverse",
            params={"accessToken": access_token},
            data={"account": account},
        )

    def verify_fediverse_otprequest(self, code: Optional[str] = None) -> Dict[str, Any]:
        """Verify Fediverse OTP code"""
        return self._request(
            "POST", "/auth/fediverse/verify", params=None, data={"code": code}
        )
