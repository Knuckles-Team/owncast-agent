# Deployment

This page covers running `owncast-agent` as a long-lived server: the transports, a
Docker Compose stack, the optional A2A agent server, putting it behind a Caddy
reverse proxy, and giving it a DNS name with Technitium. To provision the **Owncast
server** it connects to, see [Backing Platform](platform.md).

> `owncast-agent` ships an **MCP server** (console script `owncast-mcp`) and a
> companion **A2A agent server** (console script `owncast-agent`). The MCP server is
> a typed, deterministic tool surface a policy router / agent calls; the agent server
> is a Pydantic-AI agent that consumes those tools.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    owncast-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    owncast-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    owncast-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`owncast-agent` is configured entirely from the environment. The **required** set:

| Var | Default | Meaning |
|---|---|---|
| `OWNCAST_URL` | `http://localhost:9000` | Owncast server base URL |
| `OWNCAST_TOKEN` | _(empty)_ | Owncast admin / integration access token |
| `TRANSPORT` | `stdio` | MCP transport: `stdio`, `streamable-http`, `sse` |
| `HOST` | `0.0.0.0` | Bind address (HTTP transports) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `INTERNALTOOL` | `True` | Register the `internal` tool group |
| `OBJECTSTOOL` | `True` | Register the `objects` tool group |
| `EXTERNALTOOL` | `True` | Register the `external` tool group |
| `CHATTOOL` | `True` | Register the `chat` tool group |

Optional telemetry and access-governance settings (`ENABLE_OTEL`, `OTEL_*`,
`EUNOMIA_*`, `DEFAULT_AGENT_NAME`) are documented in
[`.env.example`](https://github.com/Knuckles-Team/owncast-agent/blob/main/.env.example).
Copy it to `.env` and fill in only what you use.

## Docker Compose

The repo ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/owncast-agent/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
services:
  owncast-agent-mcp:
    image: knucklessg1/owncast-agent:latest
    container_name: owncast-agent-mcp
    hostname: owncast-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```bash
cp .env.example .env          # then edit OWNCAST_URL / OWNCAST_TOKEN
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## A2A agent server

`owncast-agent` also ships a Pydantic-AI agent server (console script
`owncast-agent`). It connects to the MCP server over HTTP and exposes an A2A / AG-UI
endpoint, optionally with a web interface and OpenTelemetry tracing.

```bash
export OWNCAST_URL=http://your-owncast:8080
export OWNCAST_TOKEN=your_owncast_token
owncast-agent --provider openai --model-id gpt-4o --api-key sk-...
```

The repo ships [`docker/agent.compose.yml`](https://github.com/Knuckles-Team/owncast-agent/blob/main/docker/agent.compose.yml),
which runs the MCP server and the agent server together. The agent listens on
**`:9004`** and reaches the MCP server by container name through `MCP_URL`:

```yaml
services:
  owncast-agent-mcp:
    image: knucklessg1/owncast-agent:latest
    hostname: owncast-agent-mcp
    env_file: [../.env]
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports: ["8000:8000"]

  owncast-agent-agent:
    image: knucklessg1/owncast-agent:latest
    depends_on: [owncast-agent-mcp]
    command: ["owncast-agent"]
    env_file: [../.env]
    environment:
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://owncast-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
    ports: ["9004:9004"]
```

```bash
docker compose -f docker/agent.compose.yml up -d
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
owncast-agent.arpa {
    tls internal
    reverse_proxy owncast-agent-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
owncast-agent.example.com {
    reverse_proxy owncast-agent-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=owncast-agent.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `owncast-agent.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json`:

```json
{
  "mcpServers": {
    "owncast-agent": {
      "command": "uv",
      "args": ["run", "owncast-mcp"],
      "env": {
        "OWNCAST_URL": "http://your-owncast:8080",
        "OWNCAST_TOKEN": "your_owncast_token"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://owncast-agent.arpa/mcp` instead.
