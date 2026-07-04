from typing import Any

from owncast_agent.api.api_client_base import BaseApiClient


class OwncastApi(BaseApiClient):
    def get_chat_messages(self, access_token: str) -> dict[str, Any]:
        """Gets a list of chat messages"""
        return self._request(
            "GET", "/chat", params={"accessToken": access_token}, data=None
        )

    def register_anonymous_chat_user(
        self, x_forwarded_user: str | None = None, display_name: str | None = None
    ) -> dict[str, Any]:
        """Registers an anonymous chat user

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/chat/register",
            params={"X-Forwarded-User": x_forwarded_user},
            data={"displayName": display_name},
        )

    def update_message_visibility(
        self, access_token: str, body: dict
    ) -> dict[str, Any]:
        """Update chat message visibility

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/chat/messagevisibility",
            params={"accessToken": access_token},
            data=body,
        )

    def update_user_enabled(
        self,
        access_token: str,
        user_id: str | None = None,
        enabled: bool | None = None,
    ) -> dict[str, Any]:
        """Enable/disable a user

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/chat/users/setenabled",
            params={"accessToken": access_token},
            data={"userId": user_id, "enabled": enabled},
        )

    def get_connected_chat_clients(
        self,
    ) -> dict[str, Any]:
        """Get a detailed list of currently connected chat clients"""
        return self._request("GET", "/admin/chat/clients", params=None, data=None)

    def get_chat_messages_admin(
        self,
    ) -> dict[str, Any]:
        """Get all chat messages for the admin, unfiltered"""
        return self._request("GET", "/admin/chat/messages", params=None, data=None)

    def update_message_visibility_admin(self, body: dict) -> dict[str, Any]:
        """Update visibility of chat messages"""
        return self._request(
            "POST", "/admin/chat/messagevisibility", params=None, data=body
        )

    def update_user_enabled_admin(
        self, user_id: str | None = None, enabled: bool | None = None
    ) -> dict[str, Any]:
        """Enable or disable a user

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/admin/chat/users/setenabled",
            params=None,
            data={"userId": user_id, "enabled": enabled},
        )

    def get_disabled_users(
        self,
    ) -> dict[str, Any]:
        """Get a list of disabled users"""
        return self._request(
            "GET", "/admin/chat/users/disabled", params=None, data=None
        )

    def ban_ipaddress(self, body: dict) -> dict[str, Any]:
        """Ban an IP address"""
        return self._request(
            "POST", "/admin/chat/users/ipbans/create", params=None, data=body
        )

    def unban_ipaddress(self, body: dict) -> dict[str, Any]:
        """Remove an IP ban"""
        return self._request(
            "POST", "/admin/chat/users/ipbans/remove", params=None, data=body
        )

    def get_ipaddress_bans(
        self,
    ) -> dict[str, Any]:
        """Get all banned IP addresses"""
        return self._request("GET", "/admin/chat/users/ipbans", params=None, data=None)

    def update_user_moderator(
        self, user_id: str | None = None, is_moderator: bool | None = None
    ) -> dict[str, Any]:
        """Set moderator status for a user

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/admin/chat/users/setmoderator",
            params=None,
            data={"userId": user_id, "isModerator": is_moderator},
        )

    def get_moderators(
        self,
    ) -> dict[str, Any]:
        """Get a list of moderator users"""
        return self._request(
            "GET", "/admin/chat/users/moderators", params=None, data=None
        )

    def get_custom_emoji_list(
        self,
    ) -> dict[str, Any]:
        """Get list of custom emojis supported in the chat"""
        return self._request("GET", "/emoji", params=None, data=None)

    def upload_custom_emoji(
        self, name: str | None = None, data: str | None = None
    ) -> dict[str, Any]:
        """Upload custom emoji"""
        return self._request(
            "POST",
            "/admin/emoji/upload",
            params=None,
            data={"name": name, "data": data},
        )

    def delete_custom_emoji(self, name: str | None = None) -> dict[str, Any]:
        """Delete custom emoji"""
        return self._request(
            "POST", "/admin/emoji/delete", params=None, data={"name": name}
        )
