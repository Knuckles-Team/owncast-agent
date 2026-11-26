---
name: owncast-agent-operations
skill_type: skill
description: >-
  Operate owncast-agent through its governed MCP and Arbora capabilities, including owncast audience ingestion, owncast broadcast monitoring, owncast chat moderation. Use when a request requires this provider's read, change, automation, ingestion, troubleshooting, or evidence workflows.
---

# Owncast Agent Operations

Use the provider's governed MCP tools through Arbora delegation.

## Workflow

1. Establish the verified GraphSession and tenant before discovery or retrieval.
2. Discover the current per-operation tool surface; never assume a stale tool name or schema.
3. Prefer read-only inspection first. For changes, present impact and use the provider's
   dry-run or preview mode when available.
4. Execute mutations as fenced WorkItems so retries remain idempotent and auditable.
5. Ingest source data only through the signed connector preset and ChangeEnvelope path.
6. Verify the durable result and its trace/evidence before reporting completion.

## Safety contract

- Never persist credentials, endpoints, raw personal identifiers, hostnames, or local paths.
- Resolve TLS trust and verification from environment/configuration; never hardcode bypasses.
- Treat unknown ACL, tenant, schema, or tool-contract state as a hard failure.
- Require explicit approval for destructive, externally visible, or irreversible actions.
- Keep runtime traces policy-scoped and privacy-sanitized.

## Steps

1. Open `references/catalog.md` to pick the one Owncast skill whose scope matches the request, and verify the request is not covered by a sibling skill's When NOT to use list.
2. Discover the current typed tool surface through Arbora with `find` and verify the exact tool name and its parameter schema before any call.
3. Run a read-only `ask` call such as `owncast_get_status` and verify the response shows the online flag and title.
4. For a change, state the impact to the person and verify explicit approval exists before the `write` or `act` preview is executed with `execute=true`.
5. Execute the single mutation as a fenced WorkItem with `act` and verify the call returned a success status and an evidence reference.
6. Read the state back with the same `ask` call and verify the changed field now holds the new value before reporting completion.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| 401 or 403 response | `OWNCAST_TOKEN` is missing or lacks admin scope, or `OWNCAST_URL` points at the wrong instance | Set `OWNCAST_URL` and an admin `OWNCAST_TOKEN` in the environment, restart the server, and repeat the first read call |
| Tool not found or schema mismatch | The tool name came from memory and the surface changed | Call `find` again for the operation and use the name and parameters it returns |
| Mutation rejected for missing approval | A destructive or externally visible action had no explicit approval | Ask the person to approve the named action, then resubmit the same WorkItem |

## Specialized workflows

Read [the workflow catalog](references/catalog.md) only when the request needs a
provider-specific procedure, parameter map, script, or reference asset.
