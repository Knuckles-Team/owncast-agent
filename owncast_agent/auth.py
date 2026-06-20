from agent_utilities.core.config import setting

from .api_client import OwncastApi

_client = None


def get_client() -> OwncastApi:
    global _client
    if _client is None:
        base_url = setting("OWNCAST_URL", "http://localhost:8080")
        token = setting("OWNCAST_TOKEN", "")
        _client = OwncastApi(base_url, token)
    return _client
