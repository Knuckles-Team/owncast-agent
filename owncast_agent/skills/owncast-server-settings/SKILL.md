---
name: owncast-server-settings
skill_type: skill
description: >-
  Read and change Owncast server settings: identity, appearance, video, networking,
  storage and notifications. Do NOT use for tasks outside the owncast-agent connector.
license: MIT
tags: [owncast, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---

# Owncast server settings

Use the typed tools of the `owncast-agent` connector: one tool per upstream API operation, named `owncast_<operation>`. Each tool takes typed parameters; there is no `action` or `params_json` routing.

## Where the data lives

- **owncast-stream** (`OWNCAST_URL`): holds Stream; read with `owncast_get_status`.
- **owncast-viewers** (`OWNCAST_URL`): holds Viewer; read with `owncast_get_active_viewers`.
- **owncast-hardware** (`OWNCAST_URL`): holds HardwareSample; read with `owncast_get_hardware_stats`.
- **owncast-chat** (`OWNCAST_URL`): holds ChatMessage; read with `owncast_get_chat_messages_admin`.
- **owncast-followers** (`OWNCAST_URL`): holds Person; read with `owncast_get_followers`.

## Workflows (tool-use contracts)

Each workflow is a tool-use contract in the connector ontology. Run the steps in order; read before you write.

### `owncast-inspect-config`

1. `owncast_get_all_social_platforms` (no parameters) - Get all social platforms.
2. `owncast_get_server_config` (no parameters) - Get server config.
3. `owncast_get_web_config` (no parameters) - Get web config.

### `owncast-manage-appearance`

1. `owncast_set_custom_color_variable_values` (`value`) - Set custom color variable values.
2. `owncast_set_custom_javascript` (`body`) - Set custom javascript.
3. `owncast_set_custom_offline_message` (`body`) - Set custom offline message.
4. `owncast_set_custom_styles` (`body`) - Set custom styles.
5. `owncast_set_external_actions` (`value`) - Set external actions.
6. `owncast_set_extra_page_content` (`body`) - Set extra page content.
7. `owncast_set_favicon` (no parameters) - Set favicon.
8. `owncast_set_logo` (`body`) - Set logo.
9. `owncast_reset_favicon` (`confirm`) - Reset favicon. (destructive: ask the operator first)

### `owncast-manage-identity`

1. `owncast_set_admin_password` (`body`) - Set admin password.
2. `owncast_set_directory_enabled` (`body`) - Set directory enabled.
3. `owncast_set_disable_search_indexing` (`body`) - Set disable search indexing.
4. `owncast_set_hide_viewer_count` (`body`) - Set hide viewer count.
5. `owncast_set_nsfw` (`body`) - Set nsfw.
6. `owncast_set_server_name` (`body`) - Set server name.
7. `owncast_set_server_summary` (`body`) - Set server summary.
8. `owncast_set_server_url` (`body`) - Set server url.
9. `owncast_set_server_welcome_message` (`body`) - Set server welcome message.
10. `owncast_set_social_handles` (`value`) - Set social handles.

### `owncast-manage-notifications`

1. `owncast_set_browser_notification_configuration` (`value`) - Set browser notification configuration.
2. `owncast_set_discord_notification_configuration` (`value`) - Set discord notification configuration.

### `owncast-manage-video`

1. `owncast_set_ffmpeg_path` (`body`) - Set ffmpeg path.
2. `owncast_set_rtmpserver_port` (`body`) - Set rtmpserver port.
3. `owncast_set_s3_configuration` (`value`) - Set s3 configuration.
4. `owncast_set_socket_host_override` (`body`) - Set socket host override.
5. `owncast_set_stream_keys` (`value`) - Set stream keys.
6. `owncast_set_stream_latency_level` (`body`) - Set stream latency level.
7. `owncast_set_tags` (`body`) - Set tags.
8. `owncast_set_video_codec` (`body`) - Set video codec.
9. `owncast_set_video_serving_endpoint` (`body`) - Set video serving endpoint.
10. `owncast_set_web_server_ip` (`body`) - Set web server ip.
11. `owncast_set_web_server_port` (`body`) - Set web server port.

## Guardrails

- Never print or log the admin token, stream keys or webhook secrets.
- Read before you write: every change starts from the read steps of its contract.
- Confirm the stream is online before acting on live-only signals.
- Report a tool refusal or HTTP error as it is; never retry past a refusal or invent a result.
