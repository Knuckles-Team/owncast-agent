from typing import Any

from owncast_agent.api.api_client_base import BaseApiClient


class OwncastApi(BaseApiClient):
    def remote_follow(self, account: str | None = None) -> dict[str, Any]:
        """Request remote follow"""
        return self._request(
            "POST", "/remotefollow", params=None, data={"account": account}
        )

    def get_followers(
        self, offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """Gets the list of followers"""
        return self._request(
            "GET", "/followers", params={"offset": offset, "limit": limit}, data=None
        )

    def get_followers_admin(
        self, offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """Get followers

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "GET",
            "/admin/followers",
            params={"offset": offset, "limit": limit},
            data=None,
        )

    def get_pending_follow_requests(
        self,
    ) -> dict[str, Any]:
        """Get a list of pending follow requests"""
        return self._request("GET", "/admin/followers/pending", params=None, data=None)

    def get_blocked_and_rejected_followers(
        self,
    ) -> dict[str, Any]:
        """Get a list of rejected or blocked follows"""
        return self._request("GET", "/admin/followers/blocked", params=None, data=None)

    def approve_follower(
        self, actor_iri: str | None = None, approved: bool | None = None
    ) -> dict[str, Any]:
        """Set the following state of a follower or follow request

        CONCEPT:AU-ECO.mcp.fastmcp-middleware
        """
        return self._request(
            "POST",
            "/admin/followers/approve",
            params=None,
            data={"actorIRI": actor_iri, "approved": approved},
        )
