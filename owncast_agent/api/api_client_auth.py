from typing import Any

from owncast_agent.api.api_client_base import BaseApiClient


class OwncastApi(BaseApiClient):
    def start_indie_auth_flow(
        self, access_token: str, auth_host: str | None = None
    ) -> dict[str, Any]:
        """Begins auth flow

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/auth/indieauth",
            params={"accessToken": access_token},
            data={"authHost": auth_host},
        )

    def handle_indie_auth_redirect(self, state: str) -> dict[str, Any]:
        """Handle the redirect from an IndieAuth server to continue the auth flow

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "GET", "/auth/indieauth/callback", params={"state": state}, data=None
        )

    def handle_indie_auth_endpoint_get(
        self, client_id: str, redirect_uri: str, code_challenge: str, state: str
    ) -> dict[str, Any]:
        """Handles the IndieAuth auth endpoint

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
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
    ) -> dict[str, Any]:
        """Handles IndieAuth from form submission

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request("POST", "/auth/provider/indieauth", params=None, data=None)

    def register_fediverse_otprequest(
        self, access_token: str, account: str | None = None
    ) -> dict[str, Any]:
        """Register a Fediverse OTP request

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/auth/fediverse",
            params={"accessToken": access_token},
            data={"account": account},
        )

    def verify_fediverse_otprequest(self, code: str | None = None) -> dict[str, Any]:
        """Verify Fediverse OTP code

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST", "/auth/fediverse/verify", params=None, data={"code": code}
        )
