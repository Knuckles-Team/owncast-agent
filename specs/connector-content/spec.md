# CONN-OWNCAST-AGENT-CONNECTOR-CONTENT — The connector serves its packaged content

Owner: owncast-agent. Cross-repo IDs: `SCION-CONNECTOR-CONTROL-R071`, `SCION-CONNECTOR-CONTROL-R073`.

## Purpose and user stories

The `owncast-mcp` server serves its packaged skills, prompts and ontology to any client, with no wiring of its own.

## Delivery mapping

Component: owncast-agent connector

Code: ../../owncast_agent/__init__.py

## Why a new spec

Searched `specs/` of `owncast-agent` with `git grep` for the terms of this spec. No other spec of this repository owns the capability, so this spec owns it.

## User Scenarios & Testing

### User Story 1 - Default content (Priority: P1)

The fleet operator and the engine rely on this behaviour of `owncast-agent`: `pyproject.toml` declares `owncast-mcp` as the single `scion_sdk.connector` entry point. It is proven independently of the other stories.

**Acceptance Scenarios**:

1. **Given** the `owncast-agent` connector built from the default branch, **When** `tests/test_default_content_surfaces.py::test_default_content_surfaces` runs, **Then** `resources/list` includes `skill://` and `ontology://`; `prompts/list` includes each packaged prompt.
2. **Given** the connector is configured, **When** the behaviour of row `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R003` (pack extends only the core ontology) is exercised, **Then** no core class or property is redeclared and no retired IRI base remains. Test: `tests/test_pack_extends_core.py::test_pack_declares_no_core_term`.

### Edge Cases

- The vendor service is unreachable or rejects the credential: the connector returns the SDK typed error and never a partial result.
- An argument outside the documented inputs is refused with the SDK typed refusal and causes no effect on the vendor service.
- If `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R003` is not met, its proving test fails: pack extends only the core ontology.

## Requirements

- **FR-001**: Default content. Rows: `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R001`.
- **FR-002**: Pack extends only the core ontology. Rows: `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R003`.

## Success Criteria

- **SC-001**: `resources/list` includes `skill://` and `ontology://`; `prompts/list` includes each packaged prompt. Rows: `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R001`.
- **SC-002**: No pack term redeclares a core term and no retired IRI base remains. Rows: `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R003`.

## Assumptions

- The `owncast-agent` package keeps the entry point and module layout named in the rows.
- The shared SDK supplies the transport, authentication, retry and certification helpers the rows reuse.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R001` | plan.md Production caller chain | T-001 | tests/test_default_content_surfaces.py::test_default_content_surfaces |
| FR-002 | `CONN-OWNCAST-AGENT-CONNECTOR-CONTENT-R003` | [plan.md](plan.md) | T-003 | [test-spec.md](test-spec.md) |
