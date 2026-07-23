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

*Version: 2.0.0*

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, and guidance for provisioning the Owncast platform are maintained in
> the [official documentation](https://knuckles-team.github.io/owncast-agent/).

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

This table is auto-generated from the live server — do not edit by hand.

<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `owncast_chat` | `CHATTOOL` | Manage owncast chat operations. |
| `owncast_external` | `EXTERNALTOOL` | Manage owncast external operations. |
| `owncast_internal` | `INTERNALTOOL` | Manage owncast internal operations. |
| `owncast_objects` | `OBJECTSTOOL` | Manage owncast objects operations. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>122 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `owncast_approve_follower` | `OWNCAST_APITOOL` | Set the following state of a follower or follow request |
| `owncast_auto_update_force_quit` | `OWNCAST_APITOOL` | Force quit the server and restart it |
| `owncast_auto_update_options` | `OWNCAST_APITOOL` | Return the auto-update features that are supported for this instance |
| `owncast_auto_update_start` | `OWNCAST_APITOOL` | Begin the auto-update |
| `owncast_ban_ipaddress` | `OWNCAST_APITOOL` | Ban an IP address |
| `owncast_create_external_apiuser` | `OWNCAST_APITOOL` | Create a single access token |
| `owncast_create_webhook` | `OWNCAST_APITOOL` | Create a single webhook |
| `owncast_delete_custom_emoji` | `OWNCAST_APITOOL` | Delete custom emoji |
| `owncast_delete_external_apiuser` | `OWNCAST_APITOOL` | Delete a single external API user |
| `owncast_delete_prometheus_api` | `OWNCAST_APITOOL` | Endpoint to interface with Prometheus |
| `owncast_delete_webhook` | `OWNCAST_APITOOL` | Delete a single webhook |
| `owncast_disconnect_inbound_connection` | `OWNCAST_APITOOL` | Disconnect inbound stream |
| `owncast_external_get_chat_messages` | `OWNCAST_APITOOL` | Get chat history |
| `owncast_external_get_connected_chat_clients` | `OWNCAST_APITOOL` | Connected clients |
| `owncast_external_get_status` | `OWNCAST_APITOOL` | Get the server's status |
| `owncast_external_get_user_details` | `OWNCAST_APITOOL` | Get a user's details |
| `owncast_external_set_stream_title` | `OWNCAST_APITOOL` | Stream title |
| `owncast_external_update_message_visibility` | `OWNCAST_APITOOL` | Hide chat message |
| `owncast_get_active_viewers` | `OWNCAST_APITOOL` | Get active viewers |
| `owncast_get_all_social_platforms` | `OWNCAST_APITOOL` | Get all social platforms |
| `owncast_get_blocked_and_rejected_followers` | `OWNCAST_APITOOL` | Get a list of rejected or blocked follows |
| `owncast_get_chat_messages` | `OWNCAST_APITOOL` | Gets a list of chat messages |
| `owncast_get_chat_messages_admin` | `OWNCAST_APITOOL` | Get all chat messages for the admin, unfiltered |
| `owncast_get_connected_chat_clients` | `OWNCAST_APITOOL` | Get a detailed list of currently connected chat clients |
| `owncast_get_custom_emoji_list` | `OWNCAST_APITOOL` | Get list of custom emojis supported in the chat |
| `owncast_get_disabled_users` | `OWNCAST_APITOOL` | Get a list of disabled users |
| `owncast_get_external_apiusers` | `OWNCAST_APITOOL` | Get all access tokens |
| `owncast_get_federated_actions` | `OWNCAST_APITOOL` | Get a paginated list of federated activities |
| `owncast_get_followers` | `OWNCAST_APITOOL` | Gets the list of followers |
| `owncast_get_followers_admin` | `OWNCAST_APITOOL` | Get followers |
| `owncast_get_hardware_stats` | `OWNCAST_APITOOL` | Get the current hardware stats |
| `owncast_get_ipaddress_bans` | `OWNCAST_APITOOL` | Get all banned IP addresses |
| `owncast_get_logs` | `OWNCAST_APITOOL` | Get all logs |
| `owncast_get_moderators` | `OWNCAST_APITOOL` | Get a list of moderator users |
| `owncast_get_pending_follow_requests` | `OWNCAST_APITOOL` | Get a list of pending follow requests |
| `owncast_get_prometheus_api` | `OWNCAST_APITOOL` | Endpoint to interface with Prometheus |
| `owncast_get_server_config` | `OWNCAST_APITOOL` | Get the current server config |
| `owncast_get_status` | `OWNCAST_APITOOL` | Get the status of the server |
| `owncast_get_user_details` | `OWNCAST_APITOOL` | Get a user's details |
| `owncast_get_video_playback_metrics` | `OWNCAST_APITOOL` | Get video playback metrics |
| `owncast_get_video_stream_output_variants` | `OWNCAST_APITOOL` | Get a list of video variants available |
| `owncast_get_viewers_over_time` | `OWNCAST_APITOOL` | Get viewer count over time |
| `owncast_get_warnings` | `OWNCAST_APITOOL` | Get warning/error logs |
| `owncast_get_web_config` | `OWNCAST_APITOOL` | Get the web config |
| `owncast_get_webhooks` | `OWNCAST_APITOOL` | Get all the webhooks |
| `owncast_get_ypresponse` | `OWNCAST_APITOOL` | Get the YP protocol data |
| `owncast_handle_indie_auth_endpoint_get` | `OWNCAST_APITOOL` | Handles the IndieAuth auth endpoint |
| `owncast_handle_indie_auth_endpoint_post` | `OWNCAST_APITOOL` | Handles IndieAuth from form submission |
| `owncast_handle_indie_auth_redirect` | `OWNCAST_APITOOL` | Handle the redirect from an IndieAuth server to continue the auth flow |
| `owncast_ping` | `OWNCAST_APITOOL` | Tell the backend you're an active viewer |
| `owncast_post_prometheus_api` | `OWNCAST_APITOOL` | Endpoint to interface with Prometheus |
| `owncast_put_prometheus_api` | `OWNCAST_APITOOL` | Endpoint to interface with Prometheus |
| `owncast_register_anonymous_chat_user` | `OWNCAST_APITOOL` | Registers an anonymous chat user |
| `owncast_register_fediverse_otprequest` | `OWNCAST_APITOOL` | Register a Fediverse OTP request |
| `owncast_register_for_live_notifications` | `OWNCAST_APITOOL` | Register for notifications |
| `owncast_remote_follow` | `OWNCAST_APITOOL` | Request remote follow |
| `owncast_report_playback_metrics` | `OWNCAST_APITOOL` | Save video playback metrics for future video health recording |
| `owncast_reset_favicon` | `OWNCAST_APITOOL` | Reset favicon to default |
| `owncast_reset_ypregistration` | `OWNCAST_APITOOL` | Reset YP configuration |
| `owncast_send_chat_action` | `OWNCAST_APITOOL` | Send a user action to chat |
| `owncast_send_federated_message` | `OWNCAST_APITOOL` | Send a public message to the Fediverse from the server's user |
| `owncast_send_integration_chat_message` | `OWNCAST_APITOOL` | Send a message to chat as a specific 3rd party bot/integration based on its access token |
| `owncast_send_system_message` | `OWNCAST_APITOOL` | Send a system message to the chat |
| `owncast_send_system_message_to_connected_client` | `OWNCAST_APITOOL` | Send a system message to a single client |
| `owncast_send_user_message` | `OWNCAST_APITOOL` | Send a user message to chat |
| `owncast_set_admin_password` | `OWNCAST_APITOOL` | Change the current admin password |
| `owncast_set_browser_notification_configuration` | `OWNCAST_APITOOL` | Configure Browser notifications |
| `owncast_set_chat_disabled` | `OWNCAST_APITOOL` | Disable chat |
| `owncast_set_chat_join_messages_enabled` | `OWNCAST_APITOOL` | Enable chat for user join messages |
| `owncast_set_chat_require_authentication` | `OWNCAST_APITOOL` | Set require authentication for chat |
| `owncast_set_chat_slur_filter_enabled` | `OWNCAST_APITOOL` | Set slur filter enabled |
| `owncast_set_chat_spam_protection_enabled` | `OWNCAST_APITOOL` | Set spam protection enabled |
| `owncast_set_custom_color_variable_values` | `OWNCAST_APITOOL` | Set style/color/css values |
| `owncast_set_custom_javascript` | `OWNCAST_APITOOL` | Update custom JavaScript |
| `owncast_set_custom_offline_message` | `OWNCAST_APITOOL` | Change the offline message |
| `owncast_set_custom_styles` | `OWNCAST_APITOOL` | Update custom styles |
| `owncast_set_directory_enabled` | `OWNCAST_APITOOL` | Update directory enabled |
| `owncast_set_disable_search_indexing` | `OWNCAST_APITOOL` | Update search indexing |
| `owncast_set_discord_notification_configuration` | `OWNCAST_APITOOL` | Configure Discord notifications |
| `owncast_set_enable_established_chat_user_mode` | `OWNCAST_APITOOL` | Enable/disable chat established user mode |
| `owncast_set_external_actions` | `OWNCAST_APITOOL` | Update external action links |
| `owncast_set_extra_page_content` | `OWNCAST_APITOOL` | Change the extra page content in memory |
| `owncast_set_favicon` | `OWNCAST_APITOOL` | Upload custom favicon |
| `owncast_set_federation_activity_private` | `OWNCAST_APITOOL` | Set if federation activities are private |
| `owncast_set_federation_block_domains` | `OWNCAST_APITOOL` | Set Federation blocked domains |
| `owncast_set_federation_enabled` | `OWNCAST_APITOOL` | Enable/disable federation features |
| `owncast_set_federation_go_live_message` | `OWNCAST_APITOOL` | Set federated go live message |
| `owncast_set_federation_show_engagement` | `OWNCAST_APITOOL` | Set if fediverse engagement appears in chat |
| `owncast_set_federation_username` | `OWNCAST_APITOOL` | Set local federated username |
| `owncast_set_ffmpeg_path` | `OWNCAST_APITOOL` | Update FFMPEG path |
| `owncast_set_forbidden_username_list` | `OWNCAST_APITOOL` | Set chat usernames that are not allowed |
| `owncast_set_hide_viewer_count` | `OWNCAST_APITOOL` | Update hide viewer count |
| `owncast_set_logo` | `OWNCAST_APITOOL` | Update logo |
| `owncast_set_nsfw` | `OWNCAST_APITOOL` | Update NSFW marking |
| `owncast_set_rtmpserver_port` | `OWNCAST_APITOOL` | Update RTMP post |
| `owncast_set_s3_configuration` | `OWNCAST_APITOOL` | Update S3 configuration |
| `owncast_set_server_name` | `OWNCAST_APITOOL` | Change the server name |
| `owncast_set_server_summary` | `OWNCAST_APITOOL` | Change the server summary |
| `owncast_set_server_url` | `OWNCAST_APITOOL` | Update server url |
| `owncast_set_server_welcome_message` | `OWNCAST_APITOOL` | Change the welcome message |
| `owncast_set_social_handles` | `OWNCAST_APITOOL` | Update social handles |
| `owncast_set_socket_host_override` | `OWNCAST_APITOOL` | Update websocket host override |
| `owncast_set_stream_keys` | `OWNCAST_APITOOL` | Set an array of valid stream keys |
| `owncast_set_stream_latency_level` | `OWNCAST_APITOOL` | Set the number of video segments and duration per segment in a playlist |
| `owncast_set_stream_output_variants` | `OWNCAST_APITOOL` | Set an array of video output configurations |
| `owncast_set_stream_title` | `OWNCAST_APITOOL` | Change the stream title |
| `owncast_set_suggested_username_list` | `OWNCAST_APITOOL` | Set the suggested chat usernames that will be assigned automatically |
| `owncast_set_tags` | `OWNCAST_APITOOL` | Update server tags |
| `owncast_set_video_codec` | `OWNCAST_APITOOL` | Set video codec |
| `owncast_set_video_serving_endpoint` | `OWNCAST_APITOOL` | Update custom video serving endpoint |
| `owncast_set_web_server_ip` | `OWNCAST_APITOOL` | Update server IP address |
| `owncast_set_web_server_port` | `OWNCAST_APITOOL` | Update server port |
| `owncast_start_indie_auth_flow` | `OWNCAST_APITOOL` | Begins auth flow |
| `owncast_status_admin` | `OWNCAST_APITOOL` | Get current inboard broadcaster |
| `owncast_unban_ipaddress` | `OWNCAST_APITOOL` | Remove an IP ban |
| `owncast_update_message_visibility` | `OWNCAST_APITOOL` | Update chat message visibility |
| `owncast_update_message_visibility_admin` | `OWNCAST_APITOOL` | Update visibility of chat messages |
| `owncast_update_user_enabled` | `OWNCAST_APITOOL` | Enable/disable a user |
| `owncast_update_user_enabled_admin` | `OWNCAST_APITOOL` | Enable or disable a user |
| `owncast_update_user_moderator` | `OWNCAST_APITOOL` | Set moderator status for a user |
| `owncast_upload_custom_emoji` | `OWNCAST_APITOOL` | Upload custom emoji |
| `owncast_verify_fediverse_otprequest` | `OWNCAST_APITOOL` | Verify Fediverse OTP code |

</details>

_4 action-routed tool(s) (default) · 122 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/usage.md](docs/usage.md).

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

<!-- MCP-CONFIG-EXAMPLES:START -->

> **Install the connector-focused `[mcp]` extra.** Examples use `owncast-agent[mcp]` to add
> FastMCP / FastAPI through `agent-utilities[mcp]`; the required Agent Utilities core
> still carries `epistemic-graph[full]`. The `[agent-runtime]` extra additionally
> enables model orchestration.

#### stdio Transport (local IDEs — Cursor, Claude Desktop, VS Code)

```json
{
  "mcpServers": {
    "owncast-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "owncast-agent[mcp]",
        "owncast-mcp"
      ],
      "env": {
        "MCP_TOOL_MODE": "intent",
        "CHATTOOL": "True",
        "EXTERNALTOOL": "True",
        "INTERNALTOOL": "True",
        "OBJECTSTOOL": "True",
        "OWNCAST_TOKEN": "your_owncast_admin_or_integration_token_here",
        "OWNCAST_URL": "http://localhost:9000"
      }
    }
  }
}
```

Runtime references require an alias-aware launcher such as GraphOS. Other
launchers must omit those entries and inject the resolved values through their
own runtime secret boundary.

#### Streamable-HTTP Transport (networked / production)

```json
{
  "mcpServers": {
    "owncast-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "owncast-agent[mcp]",
        "owncast-mcp",
        "--transport",
        "streamable-http",
        "--port",
        "8000"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "MCP_TOOL_MODE": "intent",
        "CHATTOOL": "True",
        "EXTERNALTOOL": "True",
        "INTERNALTOOL": "True",
        "OBJECTSTOOL": "True",
        "OWNCAST_TOKEN": "your_owncast_admin_or_integration_token_here",
        "OWNCAST_URL": "http://localhost:9000"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed Streamable-HTTP instance by `url`:

```json
{
  "mcpServers": {
    "owncast-mcp": {
      "url": "http://localhost:8000/owncast-mcp/mcp"
    }
  }
}
```

Run a reviewed container image as a least-privilege stdio child (no
listener or published port):

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  -e MCP_TOOL_MODE=intent \
  -e CHATTOOL=True \
  -e EXTERNALTOOL=True \
  -e INTERNALTOOL=True \
  -e OBJECTSTOOL=True \
  -e OWNCAST_TOKEN=your_owncast_admin_or_integration_token_here \
  -e OWNCAST_URL=http://localhost:9000 \
  registry.example.invalid/owncast-agent@sha256:<digest> owncast-mcp
```

For containerized network HTTP, supply an authenticated TLS ingress (or
direct server TLS), exact `MCP_ALLOWED_HOSTS`, and an exact trusted-proxy
CIDR policy through the operator-owned deployment profile. The generator
does not emit an unauthenticated non-loopback listener.

_Auto-generated from the code-read env surface (`MCP_TOOL_MODE` + package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`owncast-agent` can run as a local stdio process or container, or behind a remote
network boundary. The
[Deployment guide](https://knuckles-team.github.io/owncast-agent/deployment/) carries
the detailed transport contract.

- **Local container** — launch a reviewed immutable image as a least-privilege
  stdio child with no listener or published port.
- **Remote URL** — connect through an operator-supplied authenticated HTTPS
  ingress. Keep its URL, outbound identity references, trust profile, and exact
  `MCP_ALLOWED_HOSTS` in `AgentConfig`.
<!-- END GENERATED: additional-deployment-options -->

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
    image: example/owncast-agent@sha256:<digest>
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
    image: example/owncast-agent@sha256:<digest>
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

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/deployment.md](docs/deployment.md).

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

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | `pk-...` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | `sk-...` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `OWNCAST_URL` | `http://localhost:9000` |  |
| `OWNCAST_TOKEN` | `your_owncast_admin_or_integration_token_here` |  |
| `DEFAULT_AGENT_NAME` | `Owncast Agent` |  |
| `INTERNALTOOL` | `True` |  |
| `OBJECTSTOOL` | `True` |  |
| `EXTERNALTOOL` | `True` |  |
| `CHATTOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET` | — | OIDC client secret (service-account auth) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_18 package + 14 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads, grouped by purpose.

### Connection & Credentials
| Variable | Description | Default |
|----------|-------------|---------|
| `OWNCAST_URL` | Base URL of the target Owncast instance. | `http://localhost:9000` |
| `OWNCAST_TOKEN` | Owncast Admin or Integration API token for authorized operations. | — |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse`. | `stdio` |
| `HOST` | Bind host (HTTP transports). | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports). | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both`. | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list. | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list. | — |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers). | `1` |

### Tool toggles
Each action-routed tool can be disabled individually by setting its toggle env var to `false`.
The names match the authoritative "Toggle Env Var" column in the
[Available MCP Tools](#available-mcp-tools) table above.

| Variable | Tool | Default |
|----------|------|---------|
| `INTERNALTOOL` | `owncast_internal` | `True` |
| `OBJECTSTOOL` | `owncast_objects` | `True` |
| `EXTERNALTOOL` | `owncast_external` | `True` |
| `CHATTOOL` | `owncast_chat` | `True` |

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export. | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint. | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys. | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`). | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote`. | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file. | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL. | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to. | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`). | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`). | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface. | `True` |
| `DEFAULT_AGENT_NAME` | Display name for the Graph Agent. | `Owncast Agent` |

See [`.env.example`](.env.example) for a copy-paste starting point.

---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `owncast-agent[mcp]` | Connector-focused MCP server (`agent-utilities[mcp]` — FastMCP/FastAPI + `epistemic-graph[full]`) | You only run the **MCP server** (smallest install / image) |
| `owncast-agent[agent]` | Agent runtime (`agent-utilities[agent-runtime,logfire]` — model orchestration + `epistemic-graph[full]`) | You run the **integrated agent** |
| `owncast-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# Connector-focused MCP server (includes the shared graph engine)
uv pip install "owncast-agent[mcp]"

# Agent runtime (adds model orchestration to the shared graph engine)
uv pip install "owncast-agent[agent]"

# Everything (development)
uv pip install "owncast-agent[all]"      # or: python -m pip install "owncast-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `example/owncast-agent:mcp` | `--target mcp` | `owncast-agent[mcp]` — **connector-focused**, includes `epistemic-graph[full]`; no model-orchestration stack | `owncast-mcp` |
| `example/owncast-agent@sha256:<digest>` | `--target agent` (default) | `owncast-agent[agent]` — **agent runtime**, model orchestration + `epistemic-graph[full]` | `owncast-agent` |

```bash
docker build --target mcp   -t example/owncast-agent:mcp    docker/   # connector-focused MCP server
docker build --target agent -t example/owncast-agent:agent-local docker/   # agent runtime
```

`docker/mcp.compose.yml` runs the connector-focused `:mcp` server; `docker/agent.compose.yml` runs the
agent (`immutable agent digest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

Both `[mcp]` and `[agent]` carry the **epistemic-graph** engine through the required
Agent Utilities core dependency (`epistemic-graph[full]`). The `[mcp]` extra keeps
the server connector-focused; `[agent]` additionally enables model orchestration. Local
deployments can use the bundled engine. For production or shared state, run
**epistemic-graph as a dedicated database service** and configure the runtime to use it.
Deployment recipes (single-node + Raft HA), connection configuration, and architecture
diagrams are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/owncast-agent/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/owncast-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/owncast-agent/deployment/) | run the MCP and agent servers, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/owncast-agent/usage/) | the MCP tools, the `OwncastApi` client, the CLI |
| [Backing Platform](https://knuckles-team.github.io/owncast-agent/platform/) | deploy Owncast with Docker |
| [Overview](https://knuckles-team.github.io/owncast-agent/overview/) | architecture, ecosystem role, concept index |
| [Concepts](https://knuckles-team.github.io/owncast-agent/concepts/) | concept registry (`CONCEPT:OC-*`) |

`AGENTS.md` is the canonical contributor/agent guidance.

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=example&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/example)
![GitHub User's stars](https://img.shields.io/github/stars/example)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-utilities-deployment (generated; do not edit between markers) -->

## Deploy with `agent-utilities-deployment`

Provision this package with the consolidated **`agent-utilities-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `owncast-agent` with agent-utilities-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "owncast-agent[mcp]"`, then run `owncast-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `owncast-mcp` |
| Immutable container | deploy `registry.example.invalid/owncast-agent@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-utilities-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, GraphOS delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
