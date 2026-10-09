"""Epistemic-graph ingestion -- Wire-First coverage for owncast-agent.

Exercises the real ``ingest_entities`` seam and each record mapper against a fake
``agent_connector_sdk.ingest`` transport (no engine required). The real SDK request
builder (``agent_connector_sdk.ingest.request.build_request``) still runs, so a
malformed change set is still caught by the SDK's own contract, not re-derived here;
only the final network commit is faked. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest
from epistemic_graph.generated.source_ingestion import SourceIngestionRequest

from owncast_agent.kg_ingest import (
    ingest_active_viewers,
    ingest_chat_messages,
    ingest_entities,
    ingest_followers,
    ingest_hardware_stats,
    ingest_status,
    ingest_viewers_over_time,
)


class _FakeTransport:
    """Records every submitted request; no epistemic-graph engine required."""

    def __init__(self) -> None:
        self.requests: list[SourceIngestionRequest] = []

    async def source_status(self, _connector: str, _stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: SourceIngestionRequest) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, _data: bytes) -> str:
        raise AssertionError("owncast-agent telemetry ingestion carries no media")


@pytest.fixture
def ingest() -> tuple[KnowledgeIngest, _FakeTransport]:
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


def _relation_names(request: SourceIngestionRequest) -> set[str]:
    return {rel.relation_reference.rsplit("/", 1)[-1] for rel in request.relationships}


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    res = await ingest_entities(
        [
            {"id": "a", "node_type": "Stream", "streamTitle": "live"},
            {"id": "b", "node_type": "Viewer"},
        ],
        [{"source": "b", "target": "a", "relationship": "onStream"}],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(transport.requests) == 1
    request = transport.requests[0]
    record_ids = {record.record_id for record in request.records}
    assert record_ids == {"a", "b"}
    a_record = next(r for r in request.records if r.record_id == "a")
    assert a_record.payload["streamTitle"] == "live"
    assert _relation_names(request) == {"onStream"}


@pytest.mark.asyncio
async def test_ingest_status_maps_stream(ingest):
    service, transport = ingest
    res = await ingest_status(
        {"online": True, "streamTitle": "Demo", "viewerCount": 5},
        instance="https://cast.example.com/",
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    request = transport.requests[0]
    record = next(
        r for r in request.records if r.record_id == "owncast:stream:cast.example.com"
    )
    assert record.payload["online"] is True
    assert record.payload["streamTitle"] == "Demo"
    assert record.payload["viewerCount"] == 5


@pytest.mark.asyncio
async def test_ingest_active_viewers_links_to_stream(ingest):
    service, transport = ingest
    res = await ingest_active_viewers(
        [
            {
                "clientID": "cli-1",
                "userAgent": "Firefox",
                "geo": {"countryCode": "US", "regionName": "TX"},
            }
        ],
        instance="cast.example.com",
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    request = transport.requests[0]
    record = next(
        r for r in request.records if r.record_id == "owncast:viewer:cli-1"
    )
    assert record.payload["userAgent"] == "Firefox"
    assert record.payload["geoCountryCode"] == "US"
    rel = request.relationships[0]
    assert rel.source.record_id == "owncast:viewer:cli-1"
    assert rel.target.record_id == "owncast:stream:cast.example.com"
    assert _relation_names(request) == {"onStream"}


@pytest.mark.asyncio
async def test_ingest_viewers_over_time_timeseries(ingest):
    service, transport = ingest
    res = await ingest_viewers_over_time(
        [{"time": "2026-07-04T10:00:00Z", "value": 3}],
        instance="cast.example.com",
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    request = transport.requests[0]
    nid = "owncast:viewersample:cast.example.com:2026-07-04T10:00:00Z"
    record = next(r for r in request.records if r.record_id == nid)
    assert record.payload["viewerCount"] == 3
    assert record.payload["sampledAt"] == "2026-07-04T10:00:00Z"


@pytest.mark.asyncio
async def test_ingest_hardware_stats_merges_series_by_time(ingest):
    service, transport = ingest
    res = await ingest_hardware_stats(
        {
            "cpu": [{"time": "t1", "value": 10.0}, {"time": "t2", "value": 20.0}],
            "memory": [{"time": "t1", "value": 40.0}],
            "disk": [{"time": "t2", "value": 55.0}],
        },
        instance="cast.example.com",
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 2}
    request = transport.requests[0]
    n1 = next(
        r
        for r in request.records
        if r.record_id == "owncast:hardwaresample:cast.example.com:t1"
    )
    assert n1.payload["cpuUsage"] == 10.0
    assert n1.payload["memoryUsage"] == 40.0
    n2 = next(
        r
        for r in request.records
        if r.record_id == "owncast:hardwaresample:cast.example.com:t2"
    )
    assert n2.payload["cpuUsage"] == 20.0
    assert n2.payload["diskUsage"] == 55.0


@pytest.mark.asyncio
async def test_ingest_followers_unwraps_results_and_links(ingest):
    service, transport = ingest
    res = await ingest_followers(
        {
            "results": [
                {
                    "link": "https://fed.example/@bob",
                    "name": "Bob",
                    "username": "bob",
                    "timestamp": "2026-07-01T00:00:00Z",
                }
            ],
            "total": 1,
        },
        instance="cast.example.com",
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    request = transport.requests[0]
    record = next(
        r
        for r in request.records
        if r.record_id == "owncast:person:https://fed.example/@bob"
    )
    # PersistencePrivacyGuard redacts any "username" field before persistence
    # (CONCEPT:AU-KG PII policy); "name" alone, outside person-context, is kept.
    assert record.payload["username"] == "[REDACTED_PERSON]"
    assert record.payload["actorIRI"] == "https://fed.example/@bob"
    rel = request.relationships[0]
    assert rel.source.record_id == "owncast:person:https://fed.example/@bob"
    assert rel.target.record_id == "owncast:stream:cast.example.com"
    assert _relation_names(request) == {"follows"}


@pytest.mark.asyncio
async def test_ingest_chat_messages_maps_message_and_author(ingest):
    service, transport = ingest
    res = await ingest_chat_messages(
        [
            {
                "id": "msg-1",
                "body": "hello",
                "timestamp": "2026-07-04T10:00:00Z",
                "type": "CHAT",
                "user": {"id": "u-9", "displayName": "Alice"},
            }
        ],
        instance="cast.example.com",
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 2}
    request = transport.requests[0]
    msg = next(r for r in request.records if r.record_id == "owncast:chatmessage:msg-1")
    assert msg.payload["body"] == "hello"
    # PersistencePrivacyGuard redacts any "author" field before persistence
    # (CONCEPT:AU-KG PII policy).
    assert msg.payload["author"] == "[REDACTED_PERSON]"
    person = next(r for r in request.records if r.record_id == "owncast:person:u-9")
    assert person.payload["name"] == "Alice"
    relation_pairs = {
        (rel.source.record_id, rel.target.record_id, rel.relation_reference.rsplit("/", 1)[-1])
        for rel in request.relationships
    }
    assert ("owncast:chatmessage:msg-1", "owncast:stream:cast.example.com", "onStream") in relation_pairs
    assert ("owncast:chatmessage:msg-1", "owncast:person:u-9", "sentBy") in relation_pairs


@pytest.mark.asyncio
async def test_retired_structural_alias_is_rejected(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="node_type"):
        await ingest_entities([{"id": "a", "type": "Stream"}], ingest=service)


@pytest.mark.asyncio
async def test_empty_native_ingest_is_rejected(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="at least one entity"):
        await ingest_entities([], ingest=service)
