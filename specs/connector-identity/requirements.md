# CONN-OWNCAST-AGENT-CONNECTOR-IDENTITY — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it. The generator sets each row's state in `status.json`.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-OWNCAST-AGENT-CONNECTOR-IDENTITY-R001` | **Fleet name.** `pyproject.toml` declares `owncast-mcp` as the single `scion_sdk.connector` entry point. The content pack, the manifest `connector`, the fingerprints and the ingest binding all carry `owncast-mcp`. Caller chain: `owncast-mcp` in `pyproject.toml` runs `owncast_agent.mcp_server:mcp_server`, which builds the server from the `scion_sdk.connector` entry point `owncast_agent:connector` (`owncast_agent/__init__.py:106`); `connector_name("owncast_agent")` in the SDK resolves the same entry point name for the content pack, the manifest and the ingest binding. Shape: `pyproject.toml` entry point `owncast-mcp`, the `connector_name` helper of the SDK and the `ConnectorContent`/`IngestBinding` calls under `owncast_agent/`; reuses the SDK name resolution and adds no second constant. Proving test: `tests/test_fleet_name.py::test_connector_name_is_the_fleet_name`. | Every connector name in the package is `owncast-mcp`. |
