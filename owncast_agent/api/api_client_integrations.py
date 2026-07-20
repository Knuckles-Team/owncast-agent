from typing import Any

from owncast_agent.api.api_client_base import BaseApiClient


class OwncastApi(BaseApiClient):
    def send_system_message(self, body: dict) -> dict[str, Any]:
        """Send a system message to the chat"""
        return self._request(
            "POST", "/integrations/chat/system", params=None, data=body
        )

    def send_system_message_to_connected_client(
        self, client_id: int, body: dict
    ) -> dict[str, Any]:
        """Send a system message to a single client

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            f"/integrations/chat/system/client/{client_id}",
            params=None,
            data=body,
        )

    def send_user_message(
        self,
    ) -> dict[str, Any]:
        """Send a user message to chat"""
        return self._request("POST", "/integrations/chat/user", params=None, data=None)

    def send_integration_chat_message(self, body: dict) -> dict[str, Any]:
        """Send a message to chat as a specific 3rd party bot/integration based on its access token"""
        return self._request("POST", "/integrations/chat/send", params=None, data=body)

    def send_chat_action(self, body: dict) -> dict[str, Any]:
        """Send a user action to chat"""
        return self._request(
            "POST", "/integrations/chat/action", params=None, data=body
        )

    def external_update_message_visibility(self, body: dict) -> dict[str, Any]:
        """Hide chat message"""
        return self._request(
            "POST", "/integrations/chat/messagevisibility", params=None, data=body
        )

    def external_get_status(
        self,
    ) -> dict[str, Any]:
        """Get the server's status"""
        return self._request("GET", "/integrations/status", params=None, data=None)

    def external_set_stream_title(self, body: dict) -> dict[str, Any]:
        """Stream title"""
        return self._request(
            "POST", "/integrations/streamtitle", params=None, data=body
        )

    def external_get_chat_messages(
        self,
    ) -> dict[str, Any]:
        """Get chat history"""
        return self._request("GET", "/integrations/chat", params=None, data=None)

    def external_get_connected_chat_clients(
        self,
    ) -> dict[str, Any]:
        """Connected clients"""
        return self._request("GET", "/integrations/clients", params=None, data=None)

    def external_get_user_details(self, user_id: str) -> dict[str, Any]:
        """Get a user's details"""
        return self._request(
            "GET",
            f"/integrations/moderation/chat/user/{user_id}",
            params=None,
            data=None,
        )
