# Backing Platform — Owncast

`owncast-agent` is a **client** of an [Owncast](https://owncast.online/) server. This
page provides a Docker recipe for deploying one locally to serve as the target of
`OWNCAST_URL`. For production topologies, follow the upstream
[Owncast documentation](https://owncast.online/docs/).

!!! note "Backing-system recipe"
    Each connector in the ecosystem follows the same convention — a
    `docs/platform.md` recipe for the system it integrates with, accompanied by a
    sample Compose stack that mirrors [`services/`](https://github.com/Knuckles-Team).
    Systems offered only as a managed service have no local recipe.

## Single-node deployment (Compose)

Owncast publishes the `owncast/owncast` image. The following stack runs one server
on `:8080` (HTTP) and `:1935` (RTMP ingest) with a persistent data volume:

```yaml
# docker/owncast.compose.yml
services:
  owncast:
    image: docker.io/owncast/owncast@sha256:<digest>
    container_name: owncast
    hostname: owncast
    restart: unless-stopped
    ports:
      - "8080:8080"            # web UI + REST API (HTTP)
      - "1935:1935"            # RTMP ingest
    volumes:
      - owncast_data:/app/data
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

volumes:
  owncast_data:
```

```bash
docker compose -f docker/owncast.compose.yml up -d

# Confirm the API answers
curl -s http://localhost:8080/api/status
```

The default admin credentials are `admin` / `abc123` — change the admin password
immediately, then mint an integration access token from the **Admin → Integrations →
Access Tokens** screen for `owncast-agent` to use as `OWNCAST_TOKEN`.

## Connect owncast-agent

```bash
export OWNCAST_URL=http://localhost:8080
export OWNCAST_TOKEN=your_owncast_token

owncast-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

## Combined deployment

A combined stack places Owncast and the MCP server on one Docker network, so the
server reaches Owncast by container name:

```yaml
# docker/stack.compose.yml
services:
  owncast:
    image: docker.io/owncast/owncast@sha256:<digest>
    hostname: owncast
    ports:
      - "8080:8080"
      - "1935:1935"
    volumes:
      - owncast_data:/app/data

  owncast-agent-mcp:
    image: example/owncast-agent@sha256:<digest>
    depends_on: [owncast]
    environment:
      - OWNCAST_URL=http://owncast:8080
      - OWNCAST_TOKEN=your_owncast_token
      - TRANSPORT=streamable-http
      - HOST=0.0.0.0
      - PORT=8000
    ports: ["8000:8000"]

volumes:
  owncast_data:
```

```bash
docker compose -f docker/stack.compose.yml up -d
```
