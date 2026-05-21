# Owncast Agent - A2A | AG-UI | MCP

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

*Version: 0.11.1*

## Overview

**Owncast Agent MCP Server + A2A Agent**

Agent for interacting with Owncast API

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

*   `OWNCAST_URL`: The URL of the target service.
*   `OWNCAST_TOKEN`: The API token or access token.

#### Run in stdio mode (default):
```bash
export OWNCAST_URL="http://localhost:8080"
export OWNCAST_TOKEN="your_token"
owncast-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export OWNCAST_URL="http://localhost:8080"
export OWNCAST_TOKEN="your_token"
owncast-mcp --transport "http" --host "0.0.0.0" --port "8000"
```

## A2A Agent

### Run A2A Server
```bash
export OWNCAST_URL="http://localhost:8080"
export OWNCAST_TOKEN="your_token"
owncast-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Security & Governance

This project is built on [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities), inheriting enterprise-grade security and governance features.

### Authentication & Authorization
| Feature | Description |
|---------|-------------|
| **OIDC Token Delegation** | RFC 8693 token exchange for user-context propagation from A2A → MCP |
| **Eunomia Policies** | Fine-grained, policy-driven tool authorization (`none`, `embedded`, `remote`) |
| **Scoped Credentials** | Tools execute with the caller's scoped identity where possible |
| **3LO / OAuth / API Token** | Multiple auth strategies with graceful fallback |

### Eunomia Policy Enforcement
Eunomia provides a policy enforcement point for all tool calls:
- **Embedded mode**: Load local `mcp_policies.json` for role-based access, sensitivity gating, and audit logging
- **Remote mode**: Forward authorization decisions to a central Eunomia policy server for multi-agent governance
- Enable via CLI: `--eunomia-type embedded --eunomia-policy-file mcp_policies.json`

### Runtime Protections
| Protection | Description |
|------------|-------------|
| **Tool Guard** | Sensitivity detection with human-in-the-loop approval gating |
| **Prompt Injection Defense** | Input scanning and repetition/loop guards |
| **Content Filtering** | Output schema enforcement and cost budget controls |
| **Stuck Loop Detection** | Automatic detection and recovery from agent loops |
| **Context Limit Warnings** | Proactive alerts before context window exhaustion |

### Graph Agent Architecture
The A2A agent uses `pydantic-graph` orchestration with:
- **RouterNode**: Lightweight classifier that routes queries to specialized domains
- **DomainNode**: Focused executor with only relevant tools loaded, preventing tool hallucination
- **Approval Gates**: Policy-driven approval workflows before sensitive operations
- **Usage Guards**: Budget and rate limiting enforcement

> **Production Recommendation**: Enable `--eunomia-type embedded` (or `remote`) + OIDC delegation + containerized deployment. See [`agent-utilities` documentation](https://github.com/Knuckles-Team/agent-utilities) for full policy configuration.

## Docker

### Build

```bash
docker build -t owncast-agent .
```

### Run MCP Server

```bash
docker run -d \
  --name owncast-agent \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e OWNCAST_URL="http://your-service:8080" \
  -e OWNCAST_TOKEN="your_token" \
  knucklessg1/owncast-agent:latest
```

### Deploy with Docker Compose

```yaml
services:
  owncast-agent:
    image: knucklessg1/owncast-agent:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - OWNCAST_URL=http://your-service:8080
      - OWNCAST_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "owncast": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "owncast-agent",
        "owncast-mcp"
      ],
      "env": {
        "OWNCAST_URL": "http://your-service:8080",
        "OWNCAST_TOKEN": "your_token"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install owncast-agent
```
```bash
uv pip install owncast-agent
```

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)


## MCP Configuration Examples

### stdio (recommended for local development)
```json
{
  "mcpServers": {
    "owncast": {
      "command": ".venv/bin/owncast-mcp",
      "args": [],
      "env": {
        "OWNCAST_URL": "",
        "OWNCAST_TOKEN": ""
}
    }
  }
}
```

### Streamable HTTP (recommended for production)
```json
{
  "mcpServers": {
    "owncast": {
      "url": "http://localhost:8080/owncast-mcp/mcp"
    }
  }
}
```
## Available MCP Tools

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

| Tool Name | Description |
|-----------|-------------|
| `owncast_chat` | Consolidated Action-Routed tool for chat. Methods: get_user_details |
| `owncast_external` | Consolidated Action-Routed tool for external. Methods: send_system_message, send_system_message_to_connected_client, send_user_message, send_integration_chat_message, send_chat_action, external_update_message_visibility, external_get_status, external_set_stream_title, external_get_chat_messages, external_get_connected_chat_clients, external_get_user_details |
| `owncast_internal` | Consolidated Action-Routed tool for internal. Methods: get_status, get_custom_emoji_list, get_chat_messages, register_anonymous_chat_user, update_message_visibility, update_user_enabled, get_web_config, get_ypresponse, get_all_social_platforms, get_video_stream_output_variants, ping, remote_follow, get_followers, report_playback_metrics, register_for_live_notifications, status_admin, disconnect_inbound_connection, get_server_config, get_viewers_over_time, get_active_viewers, get_hardware_stats, get_connected_chat_clients, get_chat_messages_admin, update_message_visibility_admin, update_user_enabled_admin, get_disabled_users, ban_ipaddress, unban_ipaddress, get_ipaddress_bans, update_user_moderator, get_moderators, get_logs, get_warnings, get_followers_admin, get_pending_follow_requests, get_blocked_and_rejected_followers, approve_follower, upload_custom_emoji, delete_custom_emoji, set_admin_password, set_stream_keys, set_extra_page_content, set_stream_title, set_server_welcome_message, set_chat_disabled, set_chat_join_messages_enabled, set_enable_established_chat_user_mode, set_forbidden_username_list, set_suggested_username_list, set_chat_spam_protection_enabled, set_chat_slur_filter_enabled, set_chat_require_authentication, set_video_codec, set_stream_latency_level, set_stream_output_variants, set_custom_color_variable_values, set_logo, set_favicon, reset_favicon, set_tags, set_ffmpeg_path, set_web_server_port, set_web_server_ip, set_rtmpserver_port, set_socket_host_override, set_video_serving_endpoint, set_nsfw, set_directory_enabled, set_social_handles, set_s3_configuration, set_server_url, set_external_actions, set_custom_styles, set_custom_javascript, set_hide_viewer_count, set_disable_search_indexing, set_federation_enabled, set_federation_activity_private, set_federation_show_engagement, set_federation_username, set_federation_go_live_message, set_federation_block_domains, set_discord_notification_configuration, set_browser_notification_configuration, get_webhooks, delete_webhook, create_webhook, get_external_apiusers, delete_external_apiuser, create_external_apiuser, auto_update_options, auto_update_start, auto_update_force_quit, reset_ypregistration, get_video_playback_metrics, get_prometheus_api, post_prometheus_api, put_prometheus_api, delete_prometheus_api, send_federated_message, get_federated_actions, start_indie_auth_flow, handle_indie_auth_redirect, handle_indie_auth_endpoint_get, handle_indie_auth_endpoint_post, register_fediverse_otprequest, verify_fediverse_otprequest |
| `owncast_objects` | Consolidated Action-Routed tool for objects. Methods: set_server_name, set_server_summary, set_custom_offline_message |
