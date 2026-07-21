"""Native epistemic-graph ingestion — Wire-First coverage for owncast-agent.

Exercises the real ``ingest_entities`` seam and each record mapper with a fake
ChangeEnvelope-capable engine client (no engine required), asserting the
committed AddNode/AddEdge operations and the Owncast telemetry -> typed
:Stream / :Viewer / :ViewerSample / :HardwareSample / :ChatMessage / :Person
mappings. CONCEPT:AU-KG.ingest.enterprise-source-extractor.

The fake client mirrors the canonical fixture in agent-utilities'
``tests/knowledge_graph/test_native_ingest.py`` — the shared native-ingest
primitive requires a verified ambient ``GraphSession`` (``kg:write`` scope)
plus a client exposing ``changes``/``nodes``/``rdf``/``supports()``.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest
from agent_utilities.knowledge_graph.core.session import GraphSession, use_session
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError
from agent_utilities.models.company_brain import ActorType
from agent_utilities.security.brain_context import ActorContext, use_actor

from owncast_agent.kg_ingest import (
    ingest_active_viewers,
    ingest_chat_messages,
    ingest_entities,
    ingest_followers,
    ingest_hardware_stats,
    ingest_status,
    ingest_viewers_over_time,
)


@pytest.fixture(autouse=True)
def _governed_session():
    """Provide the verified ambient GraphSession every native-ingest write requires."""
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="__commons__",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "Stream", "streamTitle": "live"},
            {"id": "b", "node_type": "Viewer"},
        ],
        [{"source": "b", "target": "a", "relationship": "onStream"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(c.changes.applied) == 1
    assert set(c.nodes.values) == {"a", "b"}
    # provenance is stamped
    assert c.nodes.values["a"]["source"] == "owncast-agent"
    assert c.nodes.values["a"]["domain"] == "owncast"
    assert c.changes.edges == [("b", "a", {"relationship": "onStream"})]


def test_ingest_status_maps_stream():
    c = _FakeClient()
    res = ingest_status(
        {"online": True, "streamTitle": "Demo", "viewerCount": 5},
        instance="https://cast.example.com/",
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["owncast:stream:cast.example.com"]
    assert node["node_type"] == "Stream"
    assert node["online"] is True
    assert node["streamTitle"] == "Demo"
    assert node["viewerCount"] == 5


def test_ingest_active_viewers_links_to_stream():
    c = _FakeClient()
    res = ingest_active_viewers(
        [
            {
                "clientID": "cli-1",
                "userAgent": "Firefox",
                "geo": {"countryCode": "US", "regionName": "TX"},
            }
        ],
        instance="cast.example.com",
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    node = c.nodes.values["owncast:viewer:cli-1"]
    assert node["node_type"] == "Viewer"
    assert node["userAgent"] == "Firefox"
    assert node["geoCountryCode"] == "US"
    assert c.changes.edges == [
        (
            "owncast:viewer:cli-1",
            "owncast:stream:cast.example.com",
            {"relationship": "onStream"},
        )
    ]


def test_ingest_viewers_over_time_timeseries():
    c = _FakeClient()
    res = ingest_viewers_over_time(
        [{"time": "2026-07-04T10:00:00Z", "value": 3}],
        instance="cast.example.com",
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    nid = "owncast:viewersample:cast.example.com:2026-07-04T10:00:00Z"
    node = c.nodes.values[nid]
    assert node["node_type"] == "ViewerSample"
    assert node["viewerCount"] == 3
    assert node["sampledAt"] == "2026-07-04T10:00:00Z"


def test_ingest_hardware_stats_merges_series_by_time():
    c = _FakeClient()
    res = ingest_hardware_stats(
        {
            "cpu": [{"time": "t1", "value": 10.0}, {"time": "t2", "value": 20.0}],
            "memory": [{"time": "t1", "value": 40.0}],
            "disk": [{"time": "t2", "value": 55.0}],
        },
        instance="cast.example.com",
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 2}
    n1 = c.nodes.values["owncast:hardwaresample:cast.example.com:t1"]
    assert n1["node_type"] == "HardwareSample"
    assert n1["cpuUsage"] == 10.0
    assert n1["memoryUsage"] == 40.0
    n2 = c.nodes.values["owncast:hardwaresample:cast.example.com:t2"]
    assert n2["cpuUsage"] == 20.0
    assert n2["diskUsage"] == 55.0


def test_ingest_followers_unwraps_results_and_links():
    c = _FakeClient()
    res = ingest_followers(
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
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    node = c.nodes.values["owncast:person:https://fed.example/@bob"]
    assert node["node_type"] == "Person"
    # native_ingest routes writes through envelope_ingest's PersistencePrivacyGuard,
    # which redacts any "username" field before persistence (CONCEPT:AU-KG PII policy).
    assert node["username"] == "[REDACTED_PERSON]"
    assert node["actorIRI"] == "https://fed.example/@bob"
    assert c.changes.edges == [
        (
            "owncast:person:https://fed.example/@bob",
            "owncast:stream:cast.example.com",
            {"relationship": "follows"},
        )
    ]


def test_ingest_chat_messages_maps_message_and_author():
    c = _FakeClient()
    res = ingest_chat_messages(
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
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 2}
    msg = c.nodes.values["owncast:chatmessage:msg-1"]
    assert msg["node_type"] == "ChatMessage"
    assert msg["body"] == "hello"
    # native_ingest routes writes through envelope_ingest's PersistencePrivacyGuard,
    # which redacts any "author" field before persistence (CONCEPT:AU-KG PII policy).
    assert msg["author"] == "[REDACTED_PERSON]"
    person = c.nodes.values["owncast:person:u-9"]
    assert person["node_type"] == "Person"
    assert person["name"] == "Alice"
    assert (
        "owncast:chatmessage:msg-1",
        "owncast:stream:cast.example.com",
        {"relationship": "onStream"},
    ) in c.changes.edges
    assert (
        "owncast:chatmessage:msg-1",
        "owncast:person:u-9",
        {"relationship": "sentBy"},
    ) in c.changes.edges


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Stream"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
