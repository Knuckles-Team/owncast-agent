"""Native epistemic-graph ingestion — Wire-First coverage for owncast-agent.

Exercises the real ``ingest_entities`` seam and each record mapper with a fake engine
client (no engine required), asserting the txn add_node/commit + edge calls and the
Owncast telemetry -> typed :Stream / :Viewer / :ViewerSample / :HardwareSample /
:ChatMessage / :Person mappings. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

from owncast_agent.kg_ingest import (
    ingest_active_viewers,
    ingest_chat_messages,
    ingest_entities,
    ingest_followers,
    ingest_hardware_stats,
    ingest_status,
    ingest_viewers_over_time,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def add_edge(self, txn, source, target, props):
        self.edges.append((source, target, props))

    def commit(self, txn):
        self.committed = True
        return True


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()


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
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "owncast-agent"
    assert c.txn.nodes["a"]["domain"] == "owncast"
    assert c.txn.edges == [("b", "a", {"relationship": "onStream"})]


def test_ingest_status_maps_stream():
    c = _FakeClient()
    res = ingest_status(
        {"online": True, "streamTitle": "Demo", "viewerCount": 5},
        instance="https://cast.example.com/",
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["owncast:stream:cast.example.com"]
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
    node = c.txn.nodes["owncast:viewer:cli-1"]
    assert node["node_type"] == "Viewer"
    assert node["userAgent"] == "Firefox"
    assert node["geoCountryCode"] == "US"
    assert c.txn.edges == [
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
    node = c.txn.nodes[nid]
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
    n1 = c.txn.nodes["owncast:hardwaresample:cast.example.com:t1"]
    assert n1["node_type"] == "HardwareSample"
    assert n1["cpuUsage"] == 10.0
    assert n1["memoryUsage"] == 40.0
    n2 = c.txn.nodes["owncast:hardwaresample:cast.example.com:t2"]
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
    node = c.txn.nodes["owncast:person:https://fed.example/@bob"]
    assert node["node_type"] == "Person"
    assert node["username"] == "bob"
    assert node["actorIRI"] == "https://fed.example/@bob"
    assert c.txn.edges == [
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
    msg = c.txn.nodes["owncast:chatmessage:msg-1"]
    assert msg["node_type"] == "ChatMessage"
    assert msg["body"] == "hello"
    assert msg["author"] == "Alice"
    person = c.txn.nodes["owncast:person:u-9"]
    assert person["node_type"] == "Person"
    assert person["name"] == "Alice"
    assert (
        "owncast:chatmessage:msg-1",
        "owncast:stream:cast.example.com",
        {"relationship": "onStream"},
    ) in c.txn.edges
    assert (
        "owncast:chatmessage:msg-1",
        "owncast:person:u-9",
        {"relationship": "sentBy"},
    ) in c.txn.edges


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Stream"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
