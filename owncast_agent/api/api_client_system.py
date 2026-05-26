from typing import Any

from owncast_agent.api.api_client_base import BaseApiClient


class OwncastApi(BaseApiClient):
    def get_status(
        self,
    ) -> dict[str, Any]:
        """Get the status of the server"""
        return self._request("GET", "/status", params=None, data=None)

    def ping(
        self,
    ) -> dict[str, Any]:
        """Tell the backend you're an active viewer"""
        return self._request("GET", "/ping", params=None, data=None)

    def status_admin(
        self,
    ) -> dict[str, Any]:
        """Get current inboard broadcaster"""
        return self._request("GET", "/admin/status", params=None, data=None)

    def disconnect_inbound_connection(
        self,
    ) -> dict[str, Any]:
        """Disconnect inbound stream"""
        return self._request("GET", "/admin/disconnect", params=None, data=None)

    def get_viewers_over_time(self, window_start: str | None = None) -> dict[str, Any]:
        """Get viewer count over time"""
        return self._request(
            "GET",
            "/admin/viewersOverTime",
            params={"windowStart": window_start},
            data=None,
        )

    def get_active_viewers(
        self,
    ) -> dict[str, Any]:
        """Get active viewers"""
        return self._request("GET", "/admin/viewers", params=None, data=None)

    def get_hardware_stats(
        self,
    ) -> dict[str, Any]:
        """Get the current hardware stats"""
        return self._request("GET", "/admin/hardwarestats", params=None, data=None)

    def get_logs(
        self,
    ) -> dict[str, Any]:
        """Get all logs"""
        return self._request("GET", "/admin/logs", params=None, data=None)

    def get_warnings(
        self,
    ) -> dict[str, Any]:
        """Get warning/error logs"""
        return self._request("GET", "/admin/logs/warnings", params=None, data=None)

    def auto_update_options(
        self,
    ) -> dict[str, Any]:
        """Return the auto-update features that are supported for this instance"""
        return self._request("GET", "/admin/update/options", params=None, data=None)

    def auto_update_start(
        self,
    ) -> dict[str, Any]:
        """Begin the auto-update"""
        return self._request("GET", "/admin/update/start", params=None, data=None)

    def auto_update_force_quit(
        self,
    ) -> dict[str, Any]:
        """Force quit the server and restart it"""
        return self._request("GET", "/admin/update/forcequit", params=None, data=None)

    def get_video_playback_metrics(
        self,
    ) -> dict[str, Any]:
        """Get video playback metrics"""
        return self._request("GET", "/admin/metrics/video", params=None, data=None)

    def get_prometheus_api(
        self,
    ) -> dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("GET", "/admin/prometheus", params=None, data=None)

    def post_prometheus_api(
        self,
    ) -> dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("POST", "/admin/prometheus", params=None, data=None)

    def put_prometheus_api(
        self,
    ) -> dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("PUT", "/admin/prometheus", params=None, data=None)

    def delete_prometheus_api(
        self,
    ) -> dict[str, Any]:
        """Endpoint to interface with Prometheus"""
        return self._request("DELETE", "/admin/prometheus", params=None, data=None)

    def send_federated_message(self, body: dict) -> dict[str, Any]:
        """Send a public message to the Fediverse from the server's user"""
        return self._request("POST", "/admin/federation/send", params=None, data=body)

    def get_federated_actions(
        self, offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """Get a paginated list of federated activities"""
        return self._request(
            "GET",
            "/admin/federation/actions",
            params={"offset": offset, "limit": limit},
            data=None,
        )

    def report_playback_metrics(self, body: dict) -> dict[str, Any]:
        """Save video playback metrics for future video health recording"""
        return self._request("POST", "/metrics/playback", params=None, data=body)

    def register_for_live_notifications(
        self,
        access_token: str,
        channel: str | None = None,
        destination: str | None = None,
    ) -> dict[str, Any]:
        """Register for notifications"""
        return self._request(
            "POST",
            "/notifications/register",
            params={"accessToken": access_token},
            data={"channel": channel, "destination": destination},
        )

    def get_user_details(self, user_id: str, access_token: str) -> dict[str, Any]:
        """Get a user's details"""
        return self._request(
            "GET",
            f"/moderation/chat/user/{user_id}",
            params={"accessToken": access_token},
            data=None,
        )

    def get_webhooks(
        self,
    ) -> dict[str, Any]:
        """Get all the webhooks"""
        return self._request("GET", "/admin/webhooks", params=None, data=None)

    def delete_webhook(self, id: int | None = None) -> dict[str, Any]:
        """Delete a single webhook"""
        return self._request(
            "POST", "/admin/webhooks/delete", params=None, data={"id": id}
        )

    def create_webhook(
        self, url: str | None = None, events: list | None = None
    ) -> dict[str, Any]:
        """Create a single webhook"""
        return self._request(
            "POST",
            "/admin/webhooks/create",
            params=None,
            data={"url": url, "events": events},
        )

    def get_external_apiusers(
        self,
    ) -> dict[str, Any]:
        """Get all access tokens"""
        return self._request("GET", "/admin/accesstokens", params=None, data=None)

    def delete_external_apiuser(self, token: str | None = None) -> dict[str, Any]:
        """Delete a single external API user"""
        return self._request(
            "POST", "/admin/accesstokens/delete", params=None, data={"token": token}
        )

    def create_external_apiuser(
        self, name: str | None = None, scopes: list | None = None
    ) -> dict[str, Any]:
        """Create a single access token"""
        return self._request(
            "POST",
            "/admin/accesstokens/create",
            params=None,
            data={"name": name, "scopes": scopes},
        )
