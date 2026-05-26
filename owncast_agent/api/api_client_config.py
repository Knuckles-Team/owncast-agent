from typing import Any

from owncast_agent.api.api_client_base import BaseApiClient


class OwncastApi(BaseApiClient):
    def get_web_config(
        self,
    ) -> dict[str, Any]:
        """Get the web config"""
        return self._request("GET", "/config", params=None, data=None)

    def get_ypresponse(
        self,
    ) -> dict[str, Any]:
        """Get the YP protocol data"""
        return self._request("GET", "/yp", params=None, data=None)

    def get_all_social_platforms(
        self,
    ) -> dict[str, Any]:
        """Get all social platforms"""
        return self._request("GET", "/socialplatforms", params=None, data=None)

    def get_video_stream_output_variants(
        self,
    ) -> dict[str, Any]:
        """Get a list of video variants available"""
        return self._request("GET", "/video/variants", params=None, data=None)

    def get_server_config(
        self,
    ) -> dict[str, Any]:
        """Get the current server config"""
        return self._request("GET", "/admin/serverconfig", params=None, data=None)

    def set_admin_password(self, body: dict) -> dict[str, Any]:
        """Change the current admin password"""
        return self._request("POST", "/admin/config/adminpass", params=None, data=body)

    def set_stream_keys(self, value: list | None = None) -> dict[str, Any]:
        """Set an array of valid stream keys"""
        return self._request(
            "POST", "/admin/config/streamkeys", params=None, data={"value": value}
        )

    def set_extra_page_content(self, body: dict) -> dict[str, Any]:
        """Change the extra page content in memory"""
        return self._request(
            "POST", "/admin/config/pagecontent", params=None, data=body
        )

    def set_stream_title(self, body: dict) -> dict[str, Any]:
        """Change the stream title"""
        return self._request(
            "POST", "/admin/config/streamtitle", params=None, data=body
        )

    def set_server_name(self, body: dict) -> dict[str, Any]:
        """Change the server name"""
        return self._request("POST", "/admin/config/name", params=None, data=body)

    def set_server_summary(self, body: dict) -> dict[str, Any]:
        """Change the server summary"""
        return self._request(
            "POST", "/admin/config/serversummary", params=None, data=body
        )

    def set_custom_offline_message(self, body: dict) -> dict[str, Any]:
        """Change the offline message"""
        return self._request(
            "POST", "/admin/config/offlinemessage", params=None, data=body
        )

    def set_server_welcome_message(self, body: dict) -> dict[str, Any]:
        """Change the welcome message"""
        return self._request(
            "POST", "/admin/config/welcomemessage", params=None, data=body
        )

    def set_chat_disabled(self, body: dict) -> dict[str, Any]:
        """Disable chat"""
        return self._request(
            "POST", "/admin/config/chat/disable", params=None, data=body
        )

    def set_chat_join_messages_enabled(self, body: dict) -> dict[str, Any]:
        """Enable chat for user join messages"""
        return self._request(
            "POST", "/admin/config/chat/joinmessagesenabled", params=None, data=body
        )

    def set_enable_established_chat_user_mode(self, body: dict) -> dict[str, Any]:
        """Enable/disable chat established user mode"""
        return self._request(
            "POST", "/admin/config/chat/establishedusermode", params=None, data=body
        )

    def set_forbidden_username_list(self, value: list | None = None) -> dict[str, Any]:
        """Set chat usernames that are not allowed"""
        return self._request(
            "POST",
            "/admin/config/chat/forbiddenusernames",
            params=None,
            data={"value": value},
        )

    def set_suggested_username_list(self, value: list | None = None) -> dict[str, Any]:
        """Set the suggested chat usernames that will be assigned automatically"""
        return self._request(
            "POST",
            "/admin/config/chat/suggestedusernames",
            params=None,
            data={"value": value},
        )

    def set_chat_spam_protection_enabled(self, body: dict) -> dict[str, Any]:
        """Set spam protection enabled"""
        return self._request(
            "POST", "/admin/config/chat/spamprotectionenabled", params=None, data=body
        )

    def set_chat_slur_filter_enabled(self, body: dict) -> dict[str, Any]:
        """Set slur filter enabled"""
        return self._request(
            "POST", "/admin/config/chat/slurfilterenabled", params=None, data=body
        )

    def set_chat_require_authentication(self, body: dict) -> dict[str, Any]:
        """Set require authentication for chat"""
        return self._request(
            "POST", "/admin/config/chat/requireauthentication", params=None, data=body
        )

    def set_video_codec(self, body: dict) -> dict[str, Any]:
        """Set video codec"""
        return self._request(
            "POST", "/admin/config/video/codec", params=None, data=body
        )

    def set_stream_latency_level(self, body: dict) -> dict[str, Any]:
        """Set the number of video segments and duration per segment in a playlist"""
        return self._request(
            "POST", "/admin/config/video/streamlatencylevel", params=None, data=body
        )

    def set_stream_output_variants(self, value: list | None = None) -> dict[str, Any]:
        """Set an array of video output configurations"""
        return self._request(
            "POST",
            "/admin/config/video/streamoutputvariants",
            params=None,
            data={"value": value},
        )

    def set_custom_color_variable_values(
        self, value: dict | None = None
    ) -> dict[str, Any]:
        """Set style/color/css values"""
        return self._request(
            "POST", "/admin/config/appearance", params=None, data={"value": value}
        )

    def set_logo(self, body: dict) -> dict[str, Any]:
        """Update logo"""
        return self._request("POST", "/admin/config/logo", params=None, data=body)

    def set_favicon(
        self,
    ) -> dict[str, Any]:
        """Upload custom favicon"""
        return self._request("POST", "/admin/config/favicon", params=None, data=None)

    def reset_favicon(
        self,
    ) -> dict[str, Any]:
        """Reset favicon to default"""
        return self._request("DELETE", "/admin/config/favicon", params=None, data=None)

    def set_tags(self, body: dict) -> dict[str, Any]:
        """Update server tags"""
        return self._request("POST", "/admin/config/tags", params=None, data=body)

    def set_ffmpeg_path(self, body: dict) -> dict[str, Any]:
        """Update FFMPEG path"""
        return self._request("POST", "/admin/config/ffmpegpath", params=None, data=body)

    def set_web_server_port(self, body: dict) -> dict[str, Any]:
        """Update server port"""
        return self._request(
            "POST", "/admin/config/webserverport", params=None, data=body
        )

    def set_web_server_ip(self, body: dict) -> dict[str, Any]:
        """Update server IP address"""
        return self._request(
            "POST", "/admin/config/webserverip", params=None, data=body
        )

    def set_rtmpserver_port(self, body: dict) -> dict[str, Any]:
        """Update RTMP post"""
        return self._request(
            "POST", "/admin/config/rtmpserverport", params=None, data=body
        )

    def set_socket_host_override(self, body: dict) -> dict[str, Any]:
        """Update websocket host override"""
        return self._request(
            "POST", "/admin/config/sockethostoverride", params=None, data=body
        )

    def set_video_serving_endpoint(self, body: dict) -> dict[str, Any]:
        """Update custom video serving endpoint"""
        return self._request(
            "POST", "/admin/config/videoservingendpoint", params=None, data=body
        )

    def set_nsfw(self, body: dict) -> dict[str, Any]:
        """Update NSFW marking"""
        return self._request("POST", "/admin/config/nsfw", params=None, data=body)

    def set_directory_enabled(self, body: dict) -> dict[str, Any]:
        """Update directory enabled"""
        return self._request(
            "POST", "/admin/config/directoryenabled", params=None, data=body
        )

    def set_social_handles(self, value: list | None = None) -> dict[str, Any]:
        """Update social handles"""
        return self._request(
            "POST", "/admin/config/socialhandles", params=None, data={"value": value}
        )

    def set_s3_configuration(self, value: Any | None = None) -> dict[str, Any]:
        """Update S3 configuration"""
        return self._request(
            "POST", "/admin/config/s3", params=None, data={"value": value}
        )

    def set_server_url(self, body: dict) -> dict[str, Any]:
        """Update server url"""
        return self._request("POST", "/admin/config/serverurl", params=None, data=body)

    def set_external_actions(self, value: list | None = None) -> dict[str, Any]:
        """Update external action links"""
        return self._request(
            "POST", "/admin/config/externalactions", params=None, data={"value": value}
        )

    def set_custom_styles(self, body: dict) -> dict[str, Any]:
        """Update custom styles"""
        return self._request(
            "POST", "/admin/config/customstyles", params=None, data=body
        )

    def set_custom_javascript(self, body: dict) -> dict[str, Any]:
        """Update custom JavaScript"""
        return self._request(
            "POST", "/admin/config/customjavascript", params=None, data=body
        )

    def set_hide_viewer_count(self, body: dict) -> dict[str, Any]:
        """Update hide viewer count"""
        return self._request(
            "POST", "/admin/config/hideviewercount", params=None, data=body
        )

    def set_disable_search_indexing(self, body: dict) -> dict[str, Any]:
        """Update search indexing"""
        return self._request(
            "POST", "/admin/config/disablesearchindexing", params=None, data=body
        )

    def set_federation_enabled(self, body: dict) -> dict[str, Any]:
        """Enable/disable federation features"""
        return self._request(
            "POST", "/admin/config/federation/enable", params=None, data=body
        )

    def set_federation_activity_private(self, body: dict) -> dict[str, Any]:
        """Set if federation activities are private"""
        return self._request(
            "POST", "/admin/config/federation/private", params=None, data=body
        )

    def set_federation_show_engagement(self, body: dict) -> dict[str, Any]:
        """Set if fediverse engagement appears in chat"""
        return self._request(
            "POST", "/admin/config/federation/showengagement", params=None, data=body
        )

    def set_federation_username(self, body: dict) -> dict[str, Any]:
        """Set local federated username"""
        return self._request(
            "POST", "/admin/config/federation/username", params=None, data=body
        )

    def set_federation_go_live_message(self, body: dict) -> dict[str, Any]:
        """Set federated go live message"""
        return self._request(
            "POST", "/admin/config/federation/livemessage", params=None, data=body
        )

    def set_federation_block_domains(self, body: dict) -> dict[str, Any]:
        """Set Federation blocked domains"""
        return self._request(
            "POST", "/admin/config/federation/blockdomains", params=None, data=body
        )

    def set_discord_notification_configuration(
        self, value: Any | None = None
    ) -> dict[str, Any]:
        """Configure Discord notifications"""
        return self._request(
            "POST",
            "/admin/config/notifications/discord",
            params=None,
            data={"value": value},
        )

    def set_browser_notification_configuration(
        self, value: Any | None = None
    ) -> dict[str, Any]:
        """Configure Browser notifications"""
        return self._request(
            "POST",
            "/admin/config/notifications/browser",
            params=None,
            data={"value": value},
        )

    def reset_ypregistration(
        self,
    ) -> dict[str, Any]:
        """Reset YP configuration"""
        return self._request("GET", "/admin/yp/reset", params=None, data=None)
