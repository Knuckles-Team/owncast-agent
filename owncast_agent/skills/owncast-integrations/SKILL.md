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

## Steps

1. Read the current state with `owncast_get_webhooks` and verify the list shows each webhook id and its events.
2. Name the exact change to the person and verify explicit approval for `owncast_create_webhook` when it is a delete of a webhook, an external API user or the Prometheus endpoint.
3. Apply the change with `owncast_create_webhook` and verify the response returns a webhook id.
4. Read the state back with `owncast_get_webhooks` and verify the new id and url appear in the list.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| 401 or 403 response | `OWNCAST_TOKEN` is missing or lacks admin scope, or `OWNCAST_URL` points at the wrong instance | Set `OWNCAST_URL` and an admin `OWNCAST_TOKEN` in the environment, restart the server, and repeat the first read call |
| Delete refused | `confirm=true` was not passed to `owncast_delete_webhook` | Ask the operator first, then repeat with `confirm=true` |
| Webhook never fires | The events list was empty or the url is unreachable | Read `owncast_get_webhooks`, correct the events or url, and recreate with `owncast_create_webhook` |
