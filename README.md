# Owncast Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/owncast-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/owncast-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/owncast-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/owncast-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/owncast-agent)
![PyPI - License](https://img.shields.io/pypi/l/owncast-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/owncast-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/owncast-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/owncast-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/owncast-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/owncast-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/owncast-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/owncast-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/owncast-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/owncast-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/owncast-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/owncast-agent)

*Version: 0.16.0*

---

## Overview

**Owncast Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Agent for interacting with Owncast API.

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Agent for interacting with Owncast API API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Internal** | `INTERNAL_TOOL` | `True` | Manage owncast internal operations. Action-routed methods: `approve_follower`, `auto_update_force_quit`, `auto_update_options`, `auto_update_start`, `ban_ipaddress`, `create_external_apiuser`, `create_webhook`, `delete_custom_emoji`, `delete_external_apiuser`, `delete_prometheus_api`, `delete_webhook`, `disconnect_inbound_connection`, `get_active_viewers`, `get_all_social_platforms`, `get_blocked_and_rejected_followers`, `get_chat_messages`, `get_chat_messages_admin`, `get_connected_chat_clients`, `get_custom_emoji_list`, `get_disabled_users`, `get_external_apiusers`, `get_federated_actions`, `get_followers`, `get_followers_admin`, `get_hardware_stats`, `get_ipaddress_bans`, `get_logs`, `get_moderators`, `get_pending_follow_requests`, `get_prometheus_api`, `get_server_config`, `get_status`, `get_video_playback_metrics`, `get_video_stream_output_variants`, `get_viewers_over_time`, `get_warnings`, `get_web_config`, `get_webhooks`, `get_ypresponse`, `handle_indie_auth_endpoint_get`, `handle_indie_auth_endpoint_post`, `handle_indie_auth_redirect`, `ping`, `post_prometheus_api`, `put_prometheus_api`, `register_anonymous_chat_user`, `register_fediverse_otprequest`, `register_for_live_notifications`, `remote_follow`, `report_playback_metrics`, `reset_favicon`, `reset_ypregistration`, `send_federated_message`, `set_admin_password`, `set_browser_notification_configuration`, `set_chat_disabled`, `set_chat_join_messages_enabled`, `set_chat_require_authentication`, `set_chat_slur_filter_enabled`, `set_chat_spam_protection_enabled`, `set_custom_color_variable_values`, `set_custom_javascript`, `set_custom_styles`, `set_directory_enabled`, `set_disable_search_indexing`, `set_discord_notification_configuration`, `set_enable_established_chat_user_mode`, `set_external_actions`, `set_extra_page_content`, `set_favicon`, `set_federation_activity_private`, `set_federation_block_domains`, `set_federation_enabled`, `set_federation_go_live_message`, `set_federation_show_engagement`, `set_federation_username`, `set_ffmpeg_path`, `set_forbidden_username_list`, `set_hide_viewer_count`, `set_logo`, `set_nsfw`, `set_rtmpserver_port`, `set_s3_configuration`, `set_server_url`, `set_server_welcome_message`, `set_social_handles`, `set_socket_host_override`, `set_stream_keys`, `set_stream_latency_level`, `set_stream_output_variants`, `set_stream_title`, `set_suggested_username_list`, `set_tags`, `set_video_codec`, `set_video_serving_endpoint`, `set_web_server_ip`, `set_web_server_port`, `start_indie_auth_flow`, `status_admin`, `unban_ipaddress`, `update_message_visibility`, `update_message_visibility_admin`, `update_user_enabled`, `update_user_enabled_admin`, `update_user_moderator`, `upload_custom_emoji`, `verify_fediverse_otprequest`. |
| **Objects** | `OBJECTS_TOOL` | `True` | Manage owncast objects operations. Action-routed methods: `set_custom_offline_message`, `set_server_name`, `set_server_summary`. |
| **External** | `EXTERNAL_TOOL` | `True` | Manage owncast external operations. Action-routed methods: `external_get_chat_messages`, `external_get_connected_chat_clients`, `external_get_status`, `external_get_user_details`, `external_set_stream_title`, `external_update_message_visibility`, `send_chat_action`, `send_integration_chat_message`, `send_system_message`, `send_system_message_to_connected_client`, `send_user_message`. |
| **Chat** | `CHAT_TOOL` | `True` | Manage owncast chat operations. Action-routed methods: `get_user_details`. |

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](docs/mcp.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "owncast-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "owncast-agent",
        "owncast-mcp"
      ],
      "env": {
        "OWNCAST_URL": "your_owncast_url_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
Configure your client's `mcp.json` to launch the Streamable-HTTP server via `uvx` with explicit host and port definition:

```json
{
  "mcpServers": {
    "owncast-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "owncast-agent",
        "owncast-mcp"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "OWNCAST_URL": "your_owncast_url_here"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed remote or local Streamable-HTTP instance:

```json
{
  "mcpServers": {
    "owncast-agent": {
      "url": "http://localhost:8000/owncast-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name owncast-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e OWNCAST_URL="your_value" \
  knucklessg1/owncast-agent:latest
```

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export OWNCAST_URL="your_value"

# Run the agent server
owncast-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

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
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  owncast-agent-agent:
    image: knucklessg1/owncast-agent:latest
    container_name: owncast-agent-agent
    hostname: owncast-agent-agent
    restart: always
    depends_on:
      - owncast-agent-mcp
    env_file:
      - ../.env
    command: [ "owncast-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://owncast-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Environment Variables

The agent can be fully configured using the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `OWNCAST_URL` | Base URL of the target Owncast instance. | `http://localhost:8080` |
| `OWNCAST_TOKEN` | Owncast Admin or Integration API Token for authorized operations. | `""` |
| `DEFAULT_AGENT_NAME` | The default name displayed for the Graph Agent. | `Owncast Agent` |
| `AGENT_DESCRIPTION` | Detailed description of the agent shown in UI/terminal contexts. | `"AI agent for Owncast Agent operations."` |
| `AGENT_SYSTEM_PROMPT` | Custom system prompt instructions overriding workspace defaults. | *Auto-generated* |
| `INTERNAL_TOOL` / `INTERNALTOOL` | Toggle flag to enable (`True`) or disable (`False`) the Internal tools. | `True` |
| `OBJECTS_TOOL` / `OBJECTSTOOL` | Toggle flag to enable (`True`) or disable (`False`) the Objects tools. | `True` |
| `EXTERNAL_TOOL` / `EXTERNALTOOL` | Toggle flag to enable (`True`) or disable (`False`) the External tools. | `True` |
| `CHAT_TOOL` / `CHATTOOL` | Toggle flag to enable (`True`) or disable (`False`) the Chat tools. | `True` |
| `TRANSPORT` | The MCP transport protocol to run on (`stdio`, `streamable-http`, `sse`). | `stdio` |
| `HOST` | The host address to bind the HTTP/SSE server. | `localhost` |
| `PORT` | The port to bind the HTTP/SSE server. | `8000` |
| `PROVIDER` | The Pydantic AI LLM provider to use (`openai`, `anthropic`, `ollama`, etc.). | `openai` |
| `MODEL_ID` | The specific LLM model ID to execute. | `gpt-4o` |
| `ENABLE_WEB_UI` | Boolean flag to enable or disable the built-in web playground. | `True` |
| `AUTH_TYPE` | Type of authentication used for tool access controls. | `""` |
| `EUNOMIA_POLICY_FILE` | Path to the JSON file containing Eunomia tool policies. | `""` |
| `EUNOMIA_TYPE` | Eunomia policy evaluation type. | `""` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | The OTLP endpoint for OpenTelemetry metrics export. | `""` |

---

## Installation

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install owncast-agent[all]

# Using standard pip
python -m pip install owncast-agent[all]
```

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`
