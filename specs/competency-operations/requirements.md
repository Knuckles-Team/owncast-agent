# CONN-OWNCAST-AGENT-COMPETENCY-OPERATIONS — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it. The generator sets each row's state in `status.json`.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-OWNCAST-AGENT-COMPETENCY-OPERATIONS-R001` | The connector must serve an `owncast_internal` stream-history action, or persist sessions, that returns each past broadcast with start, end and peak viewers. Proving test: `tests/test_stream_history.py`. | The operation returns the documented fields. |
