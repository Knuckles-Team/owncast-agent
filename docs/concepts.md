# Concept Registry — owncast-agent

> **Prefix**: `CONCEPT:OC-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:AU-ECO.messaging.native-backend-abstraction`](https://github.com/Knuckles-Team/agent-connector-sdk/blob/main/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:OW-OS.governance.oc` | Chat & Messaging | MCP tool domain `chat` — Action-routed dynamic tool registration |
| `CONCEPT:OW-OS.governance.oc-2` | External Operations | MCP tool domain `external` — Action-routed dynamic tool registration |
| `CONCEPT:OW-OS.governance.oc-3` | Internal Operations | MCP tool domain `internal` — Action-routed dynamic tool registration |
| `CONCEPT:OW-OS.governance.oc-4` | Objects Operations | MCP tool domain `objects` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-connector-sdk)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:AU-ECO.messaging.native-backend-abstraction` | Unified Toolkit Ingestion | agent-connector-sdk |
| `CONCEPT:AU-ORCH.adapter.hot-cache-invalidation` | Confidence-Gated Router | agent-connector-sdk |
| `CONCEPT:AU-OS.config.secrets-authentication` | Prompt Injection Defense | agent-connector-sdk |
| `CONCEPT:AU-OS.state.cognitive-scheduler-preemption` | Cognitive Scheduler | agent-connector-sdk |
| `CONCEPT:AU-OS.governance.reactive-multi-axis-budget` | Guardrail Engine | agent-connector-sdk |
| `CONCEPT:AU-OS.governance.wasm-micro-agent-sandbox` | Audit Logging | agent-connector-sdk |
| `CONCEPT:AU-KG.query.object-graph-mapper` | Knowledge Graph Core | agent-connector-sdk |

## Synergy with agent-connector-sdk

This project integrates with `agent-connector-sdk` via `CONCEPT:AU-ECO.messaging.native-backend-abstraction` (Unified Toolkit Ingestion). The `owncast_agent` MCP server registers its tools with the agent-connector-sdk FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all OC-* concepts.
