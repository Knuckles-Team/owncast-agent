---
name: owncast-broadcast-monitoring
skill_type: skill
description: >-
  Monitor an Owncast live broadcast via the owncast-agent MCP server — read stream
  status (online state, title, viewer counts), active viewers, viewers-over-time and
  hardware-utilisation timeseries, and the admin broadcaster status. Use when the agent
  must check whether a stream is live, inspect concurrent audience, diagnose CPU / memory /
  disk pressure, or disconnect a stuck inbound stream. Do NOT use for chat moderation
  (owncast-chat-moderation) or pushing telemetry into the knowledge graph
  (owncast-audience-ingestion); prefer those.
license: MIT
tags: [owncast, streaming, monitoring, telemetry, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# Owncast Broadcast Monitoring

Domain-typed access to the Owncast **broadcast + telemetry** surface for live-stream
health checks. Prefer the typed `owncast_*` tools over raw
HTTP — it carries the Owncast endpoint conventions and returns stream-shaped records.

## When to use
- Check whether the stream is live (`online`) and read its title / viewer counts.
- Inspect currently connected viewers (clientID, user-agent, geo).
- Pull viewers-over-time or hardware-stats timeseries to spot drop-offs or resource pressure.
- Read the admin broadcaster status or disconnect a stuck inbound stream.

## When NOT to use
- Chat message moderation, bans, or moderators → `owncast-chat-moderation`.
- Persisting telemetry as typed KG nodes / timeseries → `owncast-audience-ingestion`.
- Follower / federation approval flows → use the typed `owncast_*` follower tools directly.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`owncast-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `OWNCAST_URL` | ✅ | Base URL of the Owncast instance (e.g. `http://localhost:8080`) |
| `OWNCAST_TOKEN` | ✅ | Admin / integration bearer token |

## Tools
Each operation is its own tool named `owncast_<operation>`; arguments are typed tool parameters.

| Typed tools |
|-------------|
| `owncast_get_status`, `owncast_status_admin`, `owncast_get_active_viewers`, `owncast_get_viewers_over_time`, `owncast_get_hardware_stats`, `owncast_disconnect_inbound_connection` |

### Key parameters
- `get_viewers_over_time` accepts an optional `window_start` (ISO timestamp) to bound the series.
- The other read actions take no parameters — pass `{}`.

## Recipes (tool arguments)
Check live status:
```json
{"tool": "owncast_get_status", "arguments": {}}
```
Read active viewers:
```json
{"tool": "owncast_get_active_viewers", "arguments": {}}
```
Viewers-over-time since a window start:
```json
{"tool": "owncast_get_viewers_over_time", "arguments": {"window_start": "2026-07-01T00:00:00Z"}}
```
Hardware stats (CPU / memory / disk series):
```json
{"tool": "owncast_get_hardware_stats", "arguments": {}}
```

## Gotchas
- `get_status` is public; `status_admin`, `get_active_viewers`, `get_hardware_stats`,
  and `disconnect_inbound_connection` are admin endpoints and need an admin token.
- When `online` is `false`, viewer and hardware series may be empty or stale — gate
  live-only decisions on `online == true`.
- `get_hardware_stats` returns three parallel timeseries (`cpu`, `memory`, `disk`), each
  a list of `{time, value}` points — align them by `time` when reasoning.

## Related
- **Persist to KG:** `owncast-audience-ingestion` maps these same reads to
  `:Stream` / `:Viewer` / `:ViewerSample` / `:HardwareSample` nodes via `owncast_ingest_telemetry`.
- **Composed by:** the `owncast_streaming_specialist` prompt.
