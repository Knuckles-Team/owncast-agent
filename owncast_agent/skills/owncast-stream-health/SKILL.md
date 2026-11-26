---
name: owncast-stream-health
skill_type: skill
description: >-
  Monitor an Owncast broadcast: stream status, viewers, hardware, playback metrics, logs,
  warnings and directory registration. Do NOT use for tasks outside the owncast-agent
  connector.
license: MIT
tags: [owncast, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---

# Owncast stream health

Use the typed tools of the `owncast-agent` connector: one tool per upstream API operation, named `owncast_<operation>`. Each tool takes typed parameters; there is no `action` or `params_json` routing.

## Where the data lives

- **owncast-stream** (`OWNCAST_URL`): holds Stream; read with `owncast_get_status`.
- **owncast-viewers** (`OWNCAST_URL`): holds Viewer; read with `owncast_get_active_viewers`.
- **owncast-hardware** (`OWNCAST_URL`): holds HardwareSample; read with `owncast_get_hardware_stats`.
- **owncast-chat** (`OWNCAST_URL`): holds ChatMessage; read with `owncast_get_chat_messages_admin`.
- **owncast-followers** (`OWNCAST_URL`): holds Person; read with `owncast_get_followers`.

## Workflows (tool-use contracts)

Each workflow is a tool-use contract in the connector ontology. Run the steps in order; read before you write.

### `owncast-manage-maintenance`

1. `owncast_auto_update_force_quit` (no parameters) - Run auto update force quit.
2. `owncast_auto_update_options` (no parameters) - Run auto update options.
3. `owncast_auto_update_start` (no parameters) - Run auto update start.

### `owncast-manage-broadcast`

1. `owncast_get_status` (no parameters) - Get status.
2. `owncast_ping` (no parameters) - Ping.
3. `owncast_status_admin` (no parameters) - Status admin.
4. `owncast_disconnect_inbound_connection` (no parameters) - Run disconnect inbound connection.
5. `owncast_set_stream_title` (`body`) - Set stream title.

### `owncast-inspect-viewers`

1. `owncast_get_active_viewers` (no parameters) - Get active viewers.
2. `owncast_get_viewers_over_time` (`window_start`) - Get viewers over time.

### `owncast-inspect-hardware`

1. `owncast_get_hardware_stats` (no parameters) - Get hardware stats.

### `owncast-manage-diagnostics`

1. `owncast_get_logs` (no parameters) - Get logs.
2. `owncast_get_warnings` (no parameters) - Get warnings.
3. `owncast_get_ypresponse` (no parameters) - Get ypresponse.
4. `owncast_reset_ypregistration` (no parameters) - Reset ypregistration. (destructive: ask the operator first)

### `owncast-manage-playback`

1. `owncast_get_video_playback_metrics` (no parameters) - Get video playback metrics.
2. `owncast_get_video_stream_output_variants` (no parameters) - Get video stream output variants.
3. `owncast_report_playback_metrics` (`body`) - Run report playback metrics.
4. `owncast_set_stream_output_variants` (`value`) - Set stream output variants.

## Guardrails

- Never print or log the admin token, stream keys or webhook secrets.
- Read before you write: every change starts from the read steps of its contract.
- Confirm the stream is online before acting on live-only signals.
- Report a tool refusal or HTTP error as it is; never retry past a refusal or invent a result.

## Steps

1. Read the current state with `owncast_get_status` and verify the online flag, title and viewer count are shown.
2. Name the exact change to the person and verify explicit approval for `owncast_set_stream_title` when it is a forced auto-update or a directory registration reset.
3. Apply the change with `owncast_set_stream_title` and verify the response reports success.
4. Read the state back with `owncast_get_status` and verify the title holds the new value.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| 401 or 403 response | `OWNCAST_TOKEN` is missing or lacks admin scope, or `OWNCAST_URL` points at the wrong instance | Set `OWNCAST_URL` and an admin `OWNCAST_TOKEN` in the environment, restart the server, and repeat the first read call |
| Stream offline | The encoder is not connected | Read `owncast_status_admin`, and with approval call `owncast_disconnect_inbound_connection` so the encoder reconnects |
| Logs or warnings empty | The window is quiet | Call `owncast_get_warnings` and `owncast_get_logs` again after the event you are chasing |
