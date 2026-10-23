# CONN-OWNCAST-AGENT-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `owncast-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `owncast_agent` from it.
