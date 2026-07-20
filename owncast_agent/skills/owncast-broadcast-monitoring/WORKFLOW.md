# Owncast Broadcast Monitoring

Monitor an Owncast live broadcast via the owncast-agent MCP server — read stream status (online state, title, viewer counts), active viewers, viewers-over-time and hardware-utilisation timeseries, and the admin broadcaster status. Use when the agent must check whether a stream is live, inspect concurrent audience, diagnose CPU / memory / disk pressure, or disconnect a stuck inbound stream. Do NOT use for chat moderation (owncast-chat-moderation) or pushing telemetry into the knowledge graph (owncast-audience-ingestion); prefer those.

# Owncast Broadcast Monitoring

Domain-typed access to the Owncast **broadcast + telemetry** surface for live-stream
health checks. Prefer the condensed `owncast_internal` action-routed tool over raw
HTTP — it carries the Owncast endpoint conventions and returns stream-shaped records.

## When to use
- Check whether the stream is live (`online`) and read its title / viewer counts.
- Inspect currently connected viewers (clientID, user-agent, geo).
- Pull viewers-over-time or hardware-stats timeseries to spot drop-offs or resource pressure.
- Read the admin broadcaster status or disconnect a stuck inbound stream.

## When NOT to use
- Chat message moderation, bans, or moderators → `owncast-chat-moderation`.
- Persisting telemetry as typed KG nodes / timeseries → `owncast-audience-ingestion`.
- Follower / federation approval flows → use `owncast_internal` follower actions directly.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`owncast-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `OWNCAST_URL` | ✅ | Base URL of the Owncast instance (e.g. `[configured-endpoint]`) |
| `OWNCAST_TOKEN` | ✅ | Admin / integration bearer token |

`MCP_TOOL_MODE` (`condensed`|`verbose`|`both`) selects the condensed action-routed
surface (used below) vs. the one-to-one verbose tools.

## Tools & actions
Prefer the **condensed** tool; it takes `action` + a `params_json` **JSON string**.

| Condensed tool | Actions (this skill) |
|----------------|----------------------|
| `owncast_internal` | `get_status`, `status_admin`, `get_active_viewers`, `get_viewers_over_time`, `get_hardware_stats`, `disconnect_inbound_connection` |

### Key parameters
- `get_viewers_over_time` accepts an optional `window_start` (ISO timestamp) to bound the series.
- The other read actions take no parameters — pass `{}`.

## Recipes (`params_json`)
Check live status:
```json
{"action": "get_status"}
```
Read active viewers:
```json
{"action": "get_active_viewers"}
```
Viewers-over-time since a window start:
```json
{"action": "get_viewers_over_time", "params_json": "{\"window_start\": \"2026-07-01T00:00:00Z\"}"}
```
Hardware stats (CPU / memory / disk series):
```json
{"action": "get_hardware_stats"}
```

## Gotchas
- `params_json` is a **string** of JSON, not an object — serialize it.
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
