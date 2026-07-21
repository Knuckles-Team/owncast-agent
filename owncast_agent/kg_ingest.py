"""Native epistemic-graph ingestion for Owncast records and telemetry.

All writes use the required ``agent_utilities.knowledge_graph.memory.native_ingest``
primitive. Nodes use canonical ``node_type`` and edges use canonical ``relationship``;
nodes and edges commit in one native transaction. Missing engine dependencies, rejected
records, conflicts, and transaction failures propagate as ``NativeIngestError``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    NativeIngestError,
)
from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_entities as _native_ingest_entities,
)

logger = logging.getLogger("owncast_agent.kg")

_SOURCE = "owncast-agent"
_DOMAIN = "owncast"


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write canonical typed nodes and relationships in one native transaction."""
    return _native_ingest_entities(
        entities,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


# --- record mappers ---------------------------------------------------------


def _instance_id(instance: str | None) -> str:
    """Normalize an instance URL/name into a stable node-id segment."""
    inst = (instance or "default").strip()
    for pre in ("https://", "http://"):
        if inst.startswith(pre):
            inst = inst[len(pre) :]
    return inst.rstrip("/") or "default"


def _stream_node_id(instance: str | None) -> str:
    return f"owncast:stream:{_instance_id(instance)}"


def ingest_status(
    status: dict[str, Any] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map an Owncast ``/status`` response → a single ``:Stream`` node."""
    if not status:
        raise NativeIngestError("Owncast status ingestion requires a status record")
    sid = _stream_node_id(instance)
    entity = {
        "id": sid,
        "node_type": "Stream",
        "instance": _instance_id(instance),
        "online": status.get("online"),
        "streamTitle": status.get("streamTitle"),
        "viewerCount": status.get("viewerCount"),
        "overallMaxViewerCount": status.get("overallMaxViewerCount"),
        "sessionMaxViewerCount": status.get("sessionMaxViewerCount"),
        "lastConnectTime": status.get("lastConnectTime"),
        "lastDisconnectTime": status.get("lastDisconnectTime"),
        "versionNumber": status.get("versionNumber"),
        "externalToolId": _instance_id(instance),
    }
    return ingest_entities([entity], client=client, graph=graph)


def ingest_active_viewers(
    viewers: list[dict[str, Any]] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map ``/admin/viewers`` records → ``:Viewer`` nodes linked ``:onStream``."""
    sid = _stream_node_id(instance)
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for v in viewers or []:
        cid = v.get("clientID") or v.get("clientId") or v.get("id")
        if cid is None:
            continue
        vid = f"owncast:viewer:{cid}"
        geo = v.get("geo") or {}
        entities.append(
            {
                "id": vid,
                "node_type": "Viewer",
                "clientID": str(cid),
                "userAgent": v.get("userAgent"),
                "connectedAt": v.get("connectedAt"),
                "messageCount": v.get("messageCount"),
                "geoCountryCode": geo.get("countryCode")
                if isinstance(geo, dict)
                else None,
                "geoRegion": geo.get("regionName") if isinstance(geo, dict) else None,
                "externalToolId": str(cid),
            }
        )
        relationships.append({"source": vid, "target": sid, "relationship": "onStream"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_viewers_over_time(
    samples: list[dict[str, Any]] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map ``/admin/viewersOverTime`` points → ``:ViewerSample`` timeseries nodes."""
    inst = _instance_id(instance)
    sid = _stream_node_id(instance)
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for s in samples or []:
        ts = s.get("time") or s.get("Time") or s.get("timestamp")
        if not ts:
            continue
        nid = f"owncast:viewersample:{inst}:{ts}"
        entities.append(
            {
                "id": nid,
                "node_type": "ViewerSample",
                "sampledAt": ts,
                "viewerCount": s.get("value", s.get("Value")),
                "instance": inst,
                "externalToolId": f"{inst}:{ts}",
            }
        )
        relationships.append({"source": nid, "target": sid, "relationship": "onStream"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_hardware_stats(
    stats: dict[str, Any] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map ``/admin/hardwarestats`` cpu/memory/disk series → ``:HardwareSample`` nodes.

    The three parallel timeseries are merged by timestamp into one sample per instant.
    """
    if not stats:
        raise NativeIngestError("Owncast hardware ingestion requires statistics")
    inst = _instance_id(instance)
    sid = _stream_node_id(instance)

    def _series(key: str) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for pt in stats.get(key) or []:
            if not isinstance(pt, dict):
                continue
            ts = pt.get("time") or pt.get("Time")
            if ts:
                out[ts] = pt.get("value", pt.get("Value"))
        return out

    cpu, mem, disk = _series("cpu"), _series("memory"), _series("disk")
    times = sorted(set(cpu) | set(mem) | set(disk))
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for ts in times:
        nid = f"owncast:hardwaresample:{inst}:{ts}"
        entities.append(
            {
                "id": nid,
                "node_type": "HardwareSample",
                "sampledAt": ts,
                "cpuUsage": cpu.get(ts),
                "memoryUsage": mem.get(ts),
                "diskUsage": disk.get(ts),
                "instance": inst,
                "externalToolId": f"{inst}:{ts}",
            }
        )
        relationships.append({"source": nid, "target": sid, "relationship": "onStream"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_followers(
    followers: list[dict[str, Any]] | dict[str, Any] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map ``/followers`` fediverse actors → ``:Person`` nodes linked ``:follows``."""
    if isinstance(followers, dict):
        followers = followers.get("results") or followers.get("data") or []
    sid = _stream_node_id(instance)
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for f in followers or []:
        actor = f.get("link") or f.get("actorIRI") or f.get("username")
        if not actor:
            continue
        pid = f"owncast:person:{actor}"
        entities.append(
            {
                "id": pid,
                "node_type": "Person",
                "name": f.get("name"),
                "username": f.get("username"),
                "actorIRI": f.get("link"),
                "image": f.get("image"),
                "followedAt": f.get("timestamp"),
                "externalToolId": actor,
            }
        )
        relationships.append({"source": pid, "target": sid, "relationship": "follows"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_chat_messages(
    messages: list[dict[str, Any]] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map admin chat messages → ``:ChatMessage`` nodes + author ``:Person`` links."""
    sid = _stream_node_id(instance)
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for m in messages or []:
        mid = m.get("id")
        if not mid:
            continue
        nid = f"owncast:chatmessage:{mid}"
        user = m.get("user") or {}
        author = user.get("displayName") or m.get("author")
        uid = user.get("id")
        entities.append(
            {
                "id": nid,
                "node_type": "ChatMessage",
                "body": m.get("body"),
                "author": author,
                "timestamp": m.get("timestamp"),
                "messageType": m.get("type"),
                "visible": m.get("visible"),
                "externalToolId": str(mid),
            }
        )
        relationships.append({"source": nid, "target": sid, "relationship": "onStream"})
        if uid:
            pid = f"owncast:person:{uid}"
            entities.append(
                {
                    "id": pid,
                    "node_type": "Person",
                    "name": author,
                    "username": user.get("displayName"),
                    "externalToolId": str(uid),
                }
            )
            relationships.append(
                {"source": nid, "target": pid, "relationship": "sentBy"}
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)
