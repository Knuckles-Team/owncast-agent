# owncast-agent

Owncast **API + MCP Server + A2A Agent** for the agent-utilities ecosystem — the
typed, deterministic control surface for an Owncast self-hosted live-streaming and
chat server.

!!! info "Official documentation"
    This site is the canonical reference for `owncast-agent`, maintained alongside
    every release.

[![PyPI](https://img.shields.io/pypi/v/owncast-agent)](https://pypi.org/project/owncast-agent/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/owncast-agent)](https://github.com/Knuckles-Team/owncast-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/owncast-agent)

## Overview

`owncast-agent` wraps the [Owncast](https://owncast.online/) admin and public REST
API with typed, deterministic MCP tools and an optional Pydantic-AI agent server. It
provides:

- **`OwncastApi`** — a `requests`-based REST client over the Owncast API, organized
  by domain (system, chat, followers, configuration, integrations, auth).
- **Action-routed MCP tools** — four togglable tool groups (`internal`, `objects`,
  `external`, `chat`) that dispatch to the client by action name, keeping the LLM
  tool surface compact.
- **An A2A agent server** — a Pydantic-AI agent (console script `owncast-agent`) that
  consumes the MCP tools, with an optional web interface and OpenTelemetry tracing.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP and agent servers, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the `OwncastApi` client, and the CLI.
- :material-database-cog: **[Backing Platform](platform.md)** — deploy Owncast with Docker.
- :material-sitemap: **[Architecture](overview.md)** — pipeline, layered client, agent topology.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:OC-*` registry.

</div>

## Quick start

```bash
pip install owncast-agent
owncast-mcp                       # stdio MCP server (default transport)
```

Connect it to an Owncast server:

```bash
export OWNCAST_URL=http://your-owncast:8080
export OWNCAST_TOKEN=your_owncast_token
owncast-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, DNS).
