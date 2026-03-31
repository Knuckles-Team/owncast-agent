import os
from typing import Dict, Any, Optional
import requests
from agent_utilities.exceptions import AuthError, ApiError

class OwncastApi:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            if response.status_code == 401:
                raise AuthError(f"Unauthorized: {response.text}")
            response.raise_for_status()
            if response.text:
                return response.json()
            return {"success": True}
        except requests.exceptions.RequestException as e:
            raise ApiError(f"API request failed: {e}")

    def get_status(self) -> Dict[str, Any]:
        return self._request("GET", "/api/status")

    def get_config(self) -> Dict[str, Any]:
        return self._request("GET", "/api/config")

    def send_chat_message(self, author: str, body: str) -> Dict[str, Any]:
        return self._request("POST", "/api/integrations/chat/send", data={"author": author, "body": body})

    def send_system_message(self, body: str) -> Dict[str, Any]:
        return self._request("POST", "/api/integrations/chat/system", data={"body": body})

    def send_action_message(self, author: str, body: str) -> Dict[str, Any]:
        return self._request("POST", "/api/integrations/chat/action", data={"author": author, "body": body})

    def get_chat_history(self) -> Dict[str, Any]:
        return self._request("GET", "/api/integrations/chat")
