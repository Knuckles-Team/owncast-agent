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

*Version: 0.12.0*

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

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](file:///home/apps/workspace/agent-packages/agents/owncast-agent/docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Internal** | `INTERNALTOOL` | `True` | Manage owncast internal operations. Action-routed methods: `get_status`, `get_custom_emoji_list`, `get_chat_messages`, `register_anonymous_chat_user`, `update_message_visibility`, `update_user_enabled`, `get_web_config`, `get_ypresponse`, `get_all_social_platforms`, `get_video_stream_output_variants`, `ping`, `remote_follow`, `get_followers`, `report_playback_metrics`, `register_for_live_notifications`, `status_admin`, `disconnect_inbound_connection`, `get_server_config`, `get_viewers_over_time`, `get_active_viewers`, `get_hardware_stats`, `get_connected_chat_clients`, `get_chat_messages_admin`, `update_message_visibility_admin`, `update_user_enabled_admin`, `get_disabled_users`, `ban_ipaddress`, `unban_ipaddress`, `get_ipaddress_bans`, `update_user_moderator`, `get_moderators`, `get_logs`, `get_warnings`, `get_followers_admin`, `get_pending_follow_requests`, `get_blocked_and_rejected_followers`, `approve_follower`, `upload_custom_emoji`, `delete_custom_emoji`, `set_admin_password`, `set_stream_keys`, `set_extra_page_content`, `set_stream_title`, `set_server_welcome_message`, `set_chat_disabled`, `set_chat_join_messages_enabled`, `set_enable_established_chat_user_mode`, `set_forbidden_username_list`, `set_suggested_username_list`, `set_chat_spam_protection_enabled`, `set_chat_slur_filter_enabled`, `set_chat_require_authentication`, `set_video_codec`, `set_stream_latency_level`, `set_stream_output_variants`, `set_custom_color_variable_values`, `set_logo`, `set_favicon`, `reset_favicon`, `set_tags`, `set_ffmpeg_path`, `set_web_server_port`, `set_web_server_ip`, `set_rtmpserver_port`, `set_socket_host_override`, `set_video_serving_endpoint`, `set_nsfw`, `set_directory_enabled`, `set_social_handles`, `set_s3_configuration`, `set_server_url`, `set_external_actions`, `set_custom_styles`, `set_custom_javascript`, `set_hide_viewer_count`, `set_disable_search_indexing`, `set_federation_enabled`, `set_federation_activity_private`, `set_federation_show_engagement`, `set_federation_username`, `set_federation_go_live_message`, `set_federation_block_domains`, `set_discord_notification_configuration`, `set_browser_notification_configuration`, `get_webhooks`, `delete_webhook`, `create_webhook`, `get_external_apiusers`, `delete_external_apiuser`, `create_external_apiuser`, `auto_update_options`, `auto_update_start`, `auto_update_force_quit`, `reset_ypregistration`, `get_video_playback_metrics`, `get_prometheus_api`, `post_prometheus_api`, `put_prometheus_api`, `delete_prometheus_api`, `send_federated_message`, `get_federated_actions`, `start_indie_auth_flow`, `handle_indie_auth_redirect`, `handle_indie_auth_endpoint_get`, `handle_indie_auth_endpoint_post`, `register_fediverse_otprequest`, `verify_fediverse_otprequest`. |
| **Objects** | `OBJECTSTOOL` | `True` | Manage owncast objects operations. Action-routed methods: `set_server_name`, `set_server_summary`, `set_custom_offline_message`. |
| **External** | `EXTERNALTOOL` | `True` | Manage owncast external operations. Action-routed methods: `send_system_message`, `send_system_message_to_connected_client`, `send_user_message`, `send_integration_chat_message`, `send_chat_action`, `external_update_message_visibility`, `external_get_status`, `external_set_stream_title`, `external_get_chat_messages`, `external_get_connected_chat_clients`, `external_get_user_details`. |
| **Chat** | `CHATTOOL` | `True` | Manage owncast chat operations. Action-routed methods: `get_user_details`. |

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](file:///home/apps/workspace/agent-packages/agents/owncast-agent/docs/mcp.md).

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

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](file:///home/apps/workspace/agent-packages/agents/owncast-agent/docs/agent.md).

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
