# Usage — API / CLI / MCP

`owncast-agent` exposes the same capability three ways: as **MCP tools** an agent
calls, as a **Python API** (`OwncastApi`) you import, and as **CLI** entry points. The
tool surface and the underlying Owncast REST contract are summarized in
[Architecture](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers four action-routed tool groups.
Each tool takes an `action` name plus a `params_json` payload and dispatches to the
matching `OwncastApi` method. The groups are individually togglable through
`INTERNALTOOL`, `OBJECTSTOOL`, `EXTERNALTOOL`, and `CHATTOOL`.

| Tool | Domain | Representative actions |
|---|---|---|
| `owncast_internal` | Server, chat moderation, configuration | `get_status`, `get_active_viewers`, `get_hardware_stats`, `get_followers`, `set_stream_title`, `get_logs` |
| `owncast_objects` | Server identity objects | `set_server_name`, `set_server_summary`, `set_custom_offline_message` |
| `owncast_external` | Integration / external messaging | `send_system_message`, `send_user_message`, `external_get_status`, `external_get_chat_messages` |
| `owncast_chat` | Chat user details | `get_user_details` |

Example agent prompts that map onto these tools:

- *"What is the current server status and active viewer count?"* → `owncast_internal` (`get_status`, `get_active_viewers`)
- *"Set the stream title to 'Live coding session'"* → `owncast_internal` (`set_stream_title`)
- *"Send a system message to the chat"* → `owncast_external` (`send_system_message`)

## As a Python API

`OwncastApi` is a `requests`-based facade over the Owncast REST API, composed from
per-domain mixins (system, chat, followers, configuration, integrations, auth).

```python
from owncast_agent.api_client import OwncastApi

api = OwncastApi(
    base_url="http://your-owncast:8080",
    token="your_owncast_token",
)

# Reads
status = api.get_status()                 # server status
viewers = api.get_active_viewers()        # current active viewers
followers = api.get_followers(limit=50)   # the follower list
hardware = api.get_hardware_stats()       # CPU / memory / disk
```

Build a client straight from the environment:

```python
from owncast_agent.auth import get_client
api = get_client()        # reads OWNCAST_URL / OWNCAST_TOKEN from the environment / .env
```

### Writes

Configuration and moderation calls map to the same client:

```python
api.set_stream_title("Live coding session")
api.send_system_message({"body": "Welcome to the stream!"})
api.approve_follower(actor_iri="https://example.social/users/alice", approved=True)
```

## As a CLI

Two console scripts are installed with the package:

```bash
# Run the MCP server (stdio by default; see Deployment for HTTP transports)
owncast-mcp --transport streamable-http --host 0.0.0.0 --port 8000

# Run the A2A agent server (consumes the MCP tools)
owncast-agent --provider openai --model-id gpt-4o --api-key sk-...
```

Both expose `--help` for the full option set:

```bash
owncast-mcp --help
owncast-agent --help
```
