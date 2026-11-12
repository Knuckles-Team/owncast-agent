---
name: owncast-federation
skill_type: skill
description: >-
  Manage Owncast fediverse federation: followers, follow requests, federated messages and
  federation settings. Do NOT use for tasks outside the owncast-agent connector.
license: MIT
tags: [owncast, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---

# Owncast fediverse federation

Use the typed tools of the `owncast-agent` connector: one tool per upstream API operation, named `owncast_<operation>`. Each tool takes typed parameters; there is no `action` or `params_json` routing.

## Where the data lives

- **owncast-stream** (`OWNCAST_URL`): holds Stream; read with `owncast_get_status`.
- **owncast-viewers** (`OWNCAST_URL`): holds Viewer; read with `owncast_get_active_viewers`.
- **owncast-hardware** (`OWNCAST_URL`): holds HardwareSample; read with `owncast_get_hardware_stats`.
- **owncast-chat** (`OWNCAST_URL`): holds ChatMessage; read with `owncast_get_chat_messages_admin`.
- **owncast-followers** (`OWNCAST_URL`): holds Person; read with `owncast_get_followers`.

## Workflows (tool-use contracts)

Each workflow is a tool-use contract in the connector ontology. Run the steps in order; read before you write.

### `owncast-manage-follower`

1. `owncast_get_blocked_and_rejected_followers` (no parameters) - Get blocked and rejected followers.
2. `owncast_get_followers` (`limit`, `offset`) - Get followers.
3. `owncast_get_followers_admin` (`limit`, `offset`) - Get followers admin.
4. `owncast_get_pending_follow_requests` (no parameters) - Get pending follow requests.
5. `owncast_approve_follower` (`actor_iri`, `approved`) - Run approve follower.
6. `owncast_remote_follow` (`account`) - Run remote follow.

### `owncast-inspect-federated-message`

1. `owncast_get_federated_actions` (`limit`, `offset`) - Get federated actions.

### `owncast-manage-fediverse-auth`

1. `owncast_register_fediverse_otprequest` (`access_token`, `account`) - Register fediverse otprequest.
2. `owncast_verify_fediverse_otprequest` (`code`) - Verify fediverse otprequest.

### `owncast-manage-federation-settings`

1. `owncast_set_federation_activity_private` (`body`) - Set federation activity private.
2. `owncast_set_federation_block_domains` (`body`) - Set federation block domains.
3. `owncast_set_federation_enabled` (`body`) - Set federation enabled.
4. `owncast_set_federation_go_live_message` (`body`) - Set federation go live message.
5. `owncast_set_federation_show_engagement` (`body`) - Set federation show engagement.
6. `owncast_set_federation_username` (`body`) - Set federation username.

## Guardrails

- Never print or log the admin token, stream keys or webhook secrets.
- Read before you write: every change starts from the read steps of its contract.
- Confirm the stream is online before acting on live-only signals.
- Report a tool refusal or HTTP error as it is; never retry past a refusal or invent a result.
