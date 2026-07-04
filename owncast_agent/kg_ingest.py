"""Native epistemic-graph ingestion for Owncast records (typed graph nodes + timeseries).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The package natively pushes its
live-streaming telemetry into the ONE epistemic-graph knowledge graph as **typed OWL
nodes** — ``:Stream`` (broadcast status), ``:Viewer`` (active viewer sessions),
``:ViewerSample`` / ``:HardwareSample`` (timeseries), ``:ChatMessage``, and ``:Person``
(fediverse followers / chat authors) — plus links, using the lightweight engine client
(``GraphComputeEngine()._client`` + ``txn``), NOT the heavy in-process ingestion engine.

This is a thin mapper over the shared native-ingest primitive
(``agent_utilities.knowledge_graph.memory.native_ingest``). That primitive is not yet in
every installed ``agent_utilities``; the import is **guarded** and falls back to a
self-contained txn writer with the identical contract. Either way everything is
best-effort and engine-guarded: with no KG stack or no reachable engine, every entry
point **no-ops** (returns ``None``), so the connector keeps working with zero KG
infrastructure. Node ids follow ``owncast:<class>:<externalId>`` and every ``type``
matches a class federated by ``owncast_agent.ontology`` (``owncast.ttl``).
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("owncast_agent.kg")

_SOURCE = "owncast-agent"
_DOMAIN = "owncast"
_DEFAULT_GRAPH = "__commons__"


# --- shared-primitive seam (guarded) ---------------------------------------

try:  # pragma: no cover - exercised only where the shared primitive is installed
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_entities as _shared_ingest_entities,
    )

    _HAVE_SHARED = True
except Exception:  # noqa: BLE001 — primitive absent -> self-contained fallback
    _shared_ingest_entities = None
    _HAVE_SHARED = False


def _fallback_client() -> tuple[Any | None, str]:
    """Resolve ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        graph = getattr(engine, "graph_name", None) or _DEFAULT_GRAPH
        return client, graph
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _fallback_ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
    *,
    source: str,
    domain: str,
    client: Any | None,
    graph: str | None,
) -> dict[str, int] | None:
    """Self-contained txn writer used when the shared primitive is not installed."""
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if client is None:
        client, graph = _fallback_client()
    if client is None:
        return None
    graph = graph or _DEFAULT_GRAPH

    try:
        txn = client.txn.begin(graph=graph)
        for ent in entities:
            props = {k: v for k, v in ent.items() if k != "id" and v is not None}
            props.setdefault("source", source)
            props.setdefault("domain", domain)
            client.txn.add_node(txn, ent["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest: wrote %d nodes, %d edges", len(entities), edges)
    return {"nodes": len(entities), "edges": edges}


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph.

    ``entities``: ``[{"id":..., "type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "type":<link>}]``.
    Routes through the shared native-ingest primitive when installed, else a
    self-contained txn writer. Returns ``{"nodes":n, "edges":m}`` or ``None``
    (no engine / failure; never raises). ``client``/``graph`` may be injected (tests).
    """
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if _HAVE_SHARED and _shared_ingest_entities is not None:
        return _shared_ingest_entities(
            entities,
            relationships,
            source=_SOURCE,
            domain=_DOMAIN,
            client=client,
            graph=graph,
        )
    return _fallback_ingest_entities(
        entities,
        relationships,
        source=_SOURCE,
        domain=_DOMAIN,
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
) -> dict[str, int] | None:
    """Map an Owncast ``/status`` response → a single ``:Stream`` node."""
    if not status:
        return None
    sid = _stream_node_id(instance)
    entity = {
        "id": sid,
        "type": "Stream",
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
) -> dict[str, int] | None:
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
                "type": "Viewer",
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
        relationships.append({"source": vid, "target": sid, "type": "onStream"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_viewers_over_time(
    samples: list[dict[str, Any]] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "ViewerSample",
                "sampledAt": ts,
                "viewerCount": s.get("value", s.get("Value")),
                "instance": inst,
                "externalToolId": f"{inst}:{ts}",
            }
        )
        relationships.append({"source": nid, "target": sid, "type": "onStream"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_hardware_stats(
    stats: dict[str, Any] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map ``/admin/hardwarestats`` cpu/memory/disk series → ``:HardwareSample`` nodes.

    The three parallel timeseries are merged by timestamp into one sample per instant.
    """
    if not stats:
        return None
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
                "type": "HardwareSample",
                "sampledAt": ts,
                "cpuUsage": cpu.get(ts),
                "memoryUsage": mem.get(ts),
                "diskUsage": disk.get(ts),
                "instance": inst,
                "externalToolId": f"{inst}:{ts}",
            }
        )
        relationships.append({"source": nid, "target": sid, "type": "onStream"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_followers(
    followers: list[dict[str, Any]] | dict[str, Any] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "Person",
                "name": f.get("name"),
                "username": f.get("username"),
                "actorIRI": f.get("link"),
                "image": f.get("image"),
                "followedAt": f.get("timestamp"),
                "externalToolId": actor,
            }
        )
        relationships.append({"source": pid, "target": sid, "type": "follows"})
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_chat_messages(
    messages: list[dict[str, Any]] | None,
    *,
    instance: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "ChatMessage",
                "body": m.get("body"),
                "author": author,
                "timestamp": m.get("timestamp"),
                "messageType": m.get("type"),
                "visible": m.get("visible"),
                "externalToolId": str(mid),
            }
        )
        relationships.append({"source": nid, "target": sid, "type": "onStream"})
        if uid:
            pid = f"owncast:person:{uid}"
            entities.append(
                {
                    "id": pid,
                    "type": "Person",
                    "name": author,
                    "username": user.get("displayName"),
                    "externalToolId": str(uid),
                }
            )
            relationships.append({"source": nid, "target": pid, "type": "sentBy"})
    return ingest_entities(entities, relationships, client=client, graph=graph)
