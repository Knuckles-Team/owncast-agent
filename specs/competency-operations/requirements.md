# CONN-OWNCAST-AGENT-COMPETENCY-OPERATIONS — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it. The generator sets each row's state in `status.json`.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-OWNCAST-AGENT-COMPETENCY-OPERATIONS-R001` | The connector must serve an `owncast_internal` stream-history action, or persist sessions, that returns each past broadcast with start, end and peak viewers. Caller chain: arbora `fleet.call` reaches the `owncast_internal` tool of `owncast_agent/mcp_server.py`, whose new `stream_history` action reads persisted sessions. Shape: a `stream_history` action in the `owncast_internal` tool, backed by a session record written when a broadcast starts and ends; returns start, end and peak viewers; reuses `owncast_agent/api/`. Proving test (planned): `tests/test_stream_history.py::test_stream_history_returns_documented_fields`. | The operation returns the documented fields. |
