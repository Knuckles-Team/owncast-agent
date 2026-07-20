# Installation

`owncast-agent` is a standard Python package and a prebuilt container image. Pick the
path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A reachable **Owncast server** with an admin or integration access token — see
  [Backing Platform](platform.md) to deploy one locally.

## From PyPI (recommended)

```bash
pip install owncast-agent
```

### Optional extras

The base install ships the MCP server and the `OwncastApi` client. Install an extra
for additional capabilities:

| Extra | Install | Pulls in |
|---|---|---|
| (base) | `pip install owncast-agent` | MCP-server runtime + `OwncastApi` client (`agent-utilities[mcp]`) |
| `agent` | `pip install "owncast-agent[agent]"` | Pydantic-AI agent server + Logfire tracing |
| `all` | `pip install "owncast-agent[all]"` | MCP server, agent server, and tracing |
| `test` | `pip install "owncast-agent[test]"` | The pytest test toolchain |

```bash
# Typical: run the MCP server and the A2A agent server
pip install "owncast-agent[all]"
```

## From source

```bash
git clone https://github.com/Knuckles-Team/owncast-agent.git
cd owncast-agent
pip install -e ".[all]"          # editable install with every extra
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run owncast-mcp
```

## Prebuilt Docker image

A multi-stage runtime image is published on every release (entrypoint `owncast-mcp`):

```bash
docker pull example/owncast-agent@sha256:<digest>

docker run --rm -i \
  -e OWNCAST_URL=http://your-owncast:8080 \
  -e OWNCAST_TOKEN=your_owncast_token \
  example/owncast-agent@sha256:<digest>        # stdio transport (default)
```

For an HTTP server with a published port, and for running the agent server, see
[Deployment](deployment.md).

## Verify the install

```bash
owncast-mcp --help
owncast-agent --help
python -c "import owncast_agent; print(owncast_agent.__version__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived MCP server and agent behind Caddy + DNS.
- **[Usage](usage.md)** — call the tools, the API, and the CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
