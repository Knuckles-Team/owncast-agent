---
name: owncast-audience-ingestion
description: >-
  Natively push Owncast live-streaming telemetry into the epistemic-graph knowledge graph
  via the owncast-agent MCP server — mapping stream status, active viewers, viewers-over-time
  and hardware-stats timeseries, chat messages, and fediverse followers to typed
  :Stream / :Viewer / :ViewerSample / :HardwareSample / :ChatMessage / :Person nodes with
  :onStream / :sentBy / :follows links. Use when the agent must persist or analyse a stream's
  audience and health in the KG. Do NOT use for one-off live reads (owncast-broadcast-monitoring)
  or interactive moderation (owncast-chat-moderation); prefer those.
license: MIT
tags: [owncast, streaming, knowledge-graph, ingestion, timeseries, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Owncast Audience Ingestion

Wire-First native ingestion of Owncast telemetry into the ONE epistemic-graph knowledge
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
- Any modality with no reachable epistemic-graph engine — the tool safely no-ops
  (returns `null` per modality) rather than erroring.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`owncast-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `OWNCAST_URL` | ✅ | Base URL — also becomes the `:Stream` instance id |
| `OWNCAST_TOKEN` | ✅ | Admin token (viewers / hardware / admin chat are admin-scoped) |

A running epistemic-graph engine is optional: ingestion is best-effort and
engine-guarded. Chat ingestion additionally needs an `access_token`.

## Tools & actions
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
