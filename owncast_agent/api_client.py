from owncast_agent.api.api_client_auth import OwncastApi as AuthApi
from owncast_agent.api.api_client_chat import OwncastApi as ChatApi
from owncast_agent.api.api_client_config import OwncastApi as ConfigApi
from owncast_agent.api.api_client_followers import OwncastApi as FollowersApi
from owncast_agent.api.api_client_integrations import OwncastApi as IntegrationsApi
from owncast_agent.api.api_client_system import OwncastApi as SystemApi


class OwncastApi(
    AuthApi,
    ChatApi,
    ConfigApi,
    FollowersApi,
    IntegrationsApi,
    SystemApi,
):
    pass
