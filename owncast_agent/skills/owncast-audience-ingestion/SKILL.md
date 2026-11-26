---
name: owncast-audience-ingestion
skill_type: skill
description: >-
  Push Owncast live-streaming telemetry into the knowledge graph through the owncast-agent MCP server: stream status, viewers, hardware timeseries, chat messages and followers become typed nodes. Use when the agent must persist an audience or stream-health snapshot. Do NOT use for one-off live reads (owncast-broadcast-monitoring).
license: MIT
tags: [owncast, streaming, knowledge-graph, ingestion, timeseries, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# Owncast Audience Ingestion

Scope: Natively push Owncast live-streaming telemetry into the medulla knowledge graph via the owncast-agent MCP server — mapping stream status, active viewers, viewers-over-time and hardware-stats timeseries, chat messages, and fediverse followers to typed :Stream / :Viewer / :ViewerSample / :HardwareSample / :ChatMessage / :Person nodes with :onStream / :sentBy / :follows links. Use when the agent must persist or analyse a stream's audience and health in the KG. Do NOT use for one-off live reads (owncast-broadcast-monitoring) or interactive moderation (owncast-chat-moderation); prefer those.

Wire-First native ingestion of Owncast telemetry into the ONE medulla knowledge
graph as **typed OWL nodes + timeseries**. Backed by `owncast_agent.kg_ingest` (a thin
mapper over the shared native-ingest primitive) and surfaced as the `owncast_ingest_telemetry`
MCP tool. CONCEPT:AU-KG.ingest.enterprise-source-extractor.

## When to use
- Persist a snapshot of stream status + audience + hardware health into the KG.
- Build viewer-count / hardware-utilisation timeseries (`:ViewerSample` / `:HardwareSample`).
- Record chat messages and fediverse followers as graph nodes for later analysis.

## When NOT to use
- One-off live reads without persistence → `owncast-broadcast-monitoring`.
- Interactive chat moderation actions → `owncast-chat-moderation`.
- Any modality with no reachable medulla engine — the tool safely no-ops
  (returns `null` per modality) rather than erroring.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`owncast-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `OWNCAST_URL` | ✅ | Base URL — also becomes the `:Stream` instance id |
| `OWNCAST_TOKEN` | ✅ | Admin token (viewers / hardware / admin chat are admin-scoped) |

A running medulla engine is optional: ingestion is best-effort and
engine-guarded. Chat ingestion additionally needs an `access_token`.

## Steps

1. Confirm the configuration by calling `owncast_get_status` and verify the response contains the stream title and online flag.
2. Preview the ingest by calling `owncast_ingest_telemetry` through Arbora and verify the plan lists the modalities (status, viewers, hardware, chat, followers) you expect.
3. Execute `owncast_ingest_telemetry` with the plan reference and verify each modality returns a node count rather than `null`.
4. If a modality returned `null`, check that a medulla engine is reachable and that chat ingestion was given its `access_token`, and verify by rerunning only that modality.
5. Query the graph for the `:Stream` node keyed by `OWNCAST_URL` and verify it links to the new `:ViewerSample` and `:HardwareSample` nodes.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| 401 or 403 response | `OWNCAST_TOKEN` is missing or lacks admin scope, or `OWNCAST_URL` points at the wrong instance | Set `OWNCAST_URL` and an admin `OWNCAST_TOKEN` in the environment, restart the server, and repeat the first read call |
| Every modality returns null | No reachable medulla engine, so ingestion safely no-ops | Start or point to the engine through the Arbora configuration and rerun `owncast_ingest_telemetry` |
| Viewers or hardware empty | The token lacks admin scope | Replace `OWNCAST_TOKEN` with an admin token and rerun `owncast_ingest_telemetry` |

## Tools
| Tool | Purpose |
|------|---------|
| `owncast_ingest_telemetry` | List live telemetry via the client and push typed nodes + timeseries into the KG |

### Key parameters
- `include` — comma-separated modalities: `status`, `viewers`, `viewers_over_time`,
  `hardware`, `followers`, `chat` (default: all except chat unless `access_token` given).
- `access_token` — required only for the `chat` modality.

## Recipes
Full snapshot (no chat):
```json
{"include": "status,viewers,viewers_over_time,hardware,followers"}
```
Just the timeseries:
```json
{"include": "viewers_over_time,hardware"}
```
Include chat:
```json
{"include": "status,chat", "access_token": "<viewer_access_token>"}
```

## Node & id model
| Source read | Node type | Id scheme |
|-------------|-----------|-----------|
| `get_status` | `:Stream` | `owncast:stream:<instance>` |
| `get_active_viewers` | `:Viewer` `:onStream` | `owncast:viewer:<clientID>` |
| `get_viewers_over_time` | `:ViewerSample` `:onStream` | `owncast:viewersample:<instance>:<time>` |
| `get_hardware_stats` | `:HardwareSample` `:onStream` | `owncast:hardwaresample:<instance>:<time>` |
| `get_followers` | `:Person` `:follows` | `owncast:person:<actorIRI>` |
| chat messages | `:ChatMessage` `:onStream` + `:sentBy` `:Person` | `owncast:chatmessage:<id>` |

## Gotchas
- The `:Stream` id derives from `OWNCAST_URL` (scheme stripped) — one instance = one Stream node.
- Every entry point **no-ops** (returns `null`) with no KG stack / no reachable engine; a
  `null` per modality is success-with-no-engine, not an error.
- Hardware's three parallel series are merged by timestamp into one `:HardwareSample` per instant.
- `get_followers` returns `{"results": [...]}` — the mapper unwraps `results` automatically.
- Node `type` values match the classes federated by `owncast_agent.ontology` (`owncast.ttl`);
  don't invent new types without extending the ontology.

## Related
- **Ontology:** `owncast_agent/ontology/owncast.ttl` defines `:Stream`, `:Viewer`,
  `:ViewerSample`, `:HardwareSample`, `:ChatMessage` and reuses shared `:Person`.
- **Read-only twins:** `owncast-broadcast-monitoring`, `owncast-chat-moderation`.
- **Composed by:** the `owncast_streaming_specialist` prompt.
