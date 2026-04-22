from pydantic import BaseModel


class OwncastStatusResponse(BaseModel):
    online: bool
    viewerCount: int
    overallMaxViewerCount: int
    sessionMaxViewerCount: int
    lastConnectTime: str | None = None
    lastDisconnectTime: str | None = None
    streamTitle: str


class ChatMessage(BaseModel):
    author: str
    body: str


class SystemMessage(BaseModel):
    body: str


class ActionMessage(BaseModel):
    author: str
    body: str
