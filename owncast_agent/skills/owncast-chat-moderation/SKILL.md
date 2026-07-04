---
name: owncast-chat-moderation
description: >-
  Moderate an Owncast live chat via the owncast-agent MCP server — read chat messages,
  toggle message visibility, enable/disable users, grant/revoke moderator status, list
  connected clients, and manage IP bans. Use when the agent must remove abusive messages,
  silence or ban a user, promote a moderator, or audit connected chat clients. Do NOT use
  for reading stream/viewer telemetry (owncast-broadcast-monitoring) or KG ingestion
  (owncast-audience-ingestion); prefer those.
license: MIT
tags: [owncast, chat, moderation, streaming, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Owncast Chat Moderation

Domain-typed access to the Owncast **chat moderation** surface. Prefer the condensed
`owncast_internal` action-routed tool over raw HTTP — it carries the moderation endpoint
conventions and expects the Owncast field names.

## When to use
- Read chat messages (filtered public feed or unfiltered admin feed).
- Hide / restore a message (`update_message_visibility_admin`).
- Enable / disable a chat user; grant or revoke moderator status.
- Audit currently connected chat clients; create or remove IP bans.

## When NOT to use
- Stream status, viewers, or hardware telemetry → `owncast-broadcast-monitoring`.
- Pushing chat / audience data into the knowledge graph → `owncast-audience-ingestion`.
- Sending outbound system / integration chat messages → the `owncast_external` tool.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`owncast-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `OWNCAST_URL` | ✅ | Base URL of the Owncast instance |
| `OWNCAST_TOKEN` | ✅ | Admin token (moderation actions are admin-scoped) |

An `accessToken` parameter is required for the **non-admin** `get_chat_messages`
read; the admin feed and moderation actions use the server token.

## Tools & actions
Prefer the **condensed** tool; it takes `action` + a `params_json` **JSON string**.

| Condensed tool | Actions (this skill) |
|----------------|----------------------|
| `owncast_internal` | `get_chat_messages`, `get_chat_messages_admin`, `update_message_visibility_admin`, `update_user_enabled_admin`, `update_user_moderator`, `get_moderators`, `get_disabled_users`, `get_connected_chat_clients`, `ban_ipaddress`, `unban_ipaddress`, `get_ipaddress_bans` |

### Key parameters
- `update_message_visibility_admin` — `body`: `{"idArray": ["<messageId>"], "visible": false}`.
- `update_user_enabled_admin` — `userId`, `enabled` (bool).
- `update_user_moderator` — `userId`, `isModerator` (bool).
- `ban_ipaddress` / `unban_ipaddress` — `body`: `{"value": "<ip>"}` (+ optional `note`).

## Recipes (`params_json`)
Read the unfiltered admin chat feed:
```json
{"action": "get_chat_messages_admin"}
```
Hide two messages:
```json
{"action": "update_message_visibility_admin", "params_json": "{\"body\": {\"idArray\": [\"m-1\", \"m-2\"], \"visible\": false}}"}
```
Disable a user:
```json
{"action": "update_user_enabled_admin", "params_json": "{\"user_id\": \"u-42\", \"enabled\": false}"}
```
Promote a moderator:
```json
{"action": "update_user_moderator", "params_json": "{\"user_id\": \"u-42\", \"is_moderator\": true}"}
```

## Gotchas
- `params_json` is a **string** of JSON, not an object — serialize it.
- Client method params are snake_case (`user_id`, `is_moderator`); the underlying
  Owncast JSON body uses camelCase (`userId`, `isModerator`) — the client maps them.
- `get_chat_messages` (public) needs an `access_token`; the admin feed does not.
- Message visibility toggles take an **array** of message ids, not a single id.

## Related
- **Read audience/telemetry:** `owncast-broadcast-monitoring`.
- **Persist chat to KG:** `owncast-audience-ingestion` maps messages to `:ChatMessage`
  nodes with `:sentBy` author `:Person` links.
- **Composed by:** the `owncast_streaming_specialist` prompt.
