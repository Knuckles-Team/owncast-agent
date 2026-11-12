---
name: owncast-integrations
skill_type: skill
description: >-
  Manage Owncast integrations: webhooks, external API users, external API calls, IndieAuth
  and the Prometheus endpoint. Do NOT use for tasks outside the owncast-agent connector.
license: MIT
tags: [owncast, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---

# Owncast integrations

Use the typed tools of the `owncast-agent` connector: one tool per upstream API operation, named `owncast_<operation>`. Each tool takes typed parameters; there is no `action` or `params_json` routing.

## Where the data lives

- **owncast-stream** (`OWNCAST_URL`): holds Stream; read with `owncast_get_status`.
- **owncast-viewers** (`OWNCAST_URL`): holds Viewer; read with `owncast_get_active_viewers`.
- **owncast-hardware** (`OWNCAST_URL`): holds HardwareSample; read with `owncast_get_hardware_stats`.
- **owncast-chat** (`OWNCAST_URL`): holds ChatMessage; read with `owncast_get_chat_messages_admin`.
- **owncast-followers** (`OWNCAST_URL`): holds Person; read with `owncast_get_followers`.

## Workflows (tool-use contracts)

Each workflow is a tool-use contract in the connector ontology. Run the steps in order; read before you write.

### `owncast-manage-api-user`

1. `owncast_get_external_apiusers` (no parameters) - Get external apiusers.
2. `owncast_create_external_apiuser` (`name`, `scopes`) - Create external apiuser.
3. `owncast_delete_external_apiuser` (`confirm`, `token`) - Delete external apiuser. (destructive: ask the operator first)

### `owncast-manage-webhook`

1. `owncast_get_webhooks` (no parameters) - Get webhooks.
2. `owncast_create_webhook` (`events`, `url`) - Create webhook.
3. `owncast_delete_webhook` (`confirm`, `id`) - Delete webhook. (destructive: ask the operator first)

### `owncast-manage-prometheus`

1. `owncast_get_prometheus_api` (no parameters) - Get prometheus api.
2. `owncast_post_prometheus_api` (no parameters) - Post prometheus api.
3. `owncast_put_prometheus_api` (no parameters) - Put prometheus api.
4. `owncast_delete_prometheus_api` (`confirm`) - Delete prometheus api. (destructive: ask the operator first)

### `owncast-manage-external-api`

1. `owncast_external_get_status` (no parameters) - Run external get status.
2. `owncast_external_set_stream_title` (`body`) - Run external set stream title.

### `owncast-manage-indie-auth`

1. `owncast_start_indie_auth_flow` (`access_token`, `auth_host`) - Start indie auth flow.
2. `owncast_handle_indie_auth_endpoint_get` (`client_id`, `code_challenge`, `redirect_uri`, `state`) - Handle indie auth endpoint get.
3. `owncast_handle_indie_auth_endpoint_post` (no parameters) - Handle indie auth endpoint post.
4. `owncast_handle_indie_auth_redirect` (`state`) - Handle indie auth redirect.

## Guardrails

- Never print or log the admin token, stream keys or webhook secrets.
- Read before you write: every change starts from the read steps of its contract.
- Confirm the stream is online before acting on live-only signals.
- Report a tool refusal or HTTP error as it is; never retry past a refusal or invent a result.
