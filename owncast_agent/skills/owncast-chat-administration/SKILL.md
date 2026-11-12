---
name: owncast-chat-administration
skill_type: skill
description: >-
  Moderate and administer Owncast chat: messages, users, moderators, IP bans, emoji,
  system messages and chat settings. Do NOT use for tasks outside the owncast-agent
  connector.
license: MIT
tags: [owncast, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---

# Owncast chat administration

Use the typed tools of the `owncast-agent` connector: one tool per upstream API operation, named `owncast_<operation>`. Each tool takes typed parameters; there is no `action` or `params_json` routing.

## Where the data lives

- **owncast-stream** (`OWNCAST_URL`): holds Stream; read with `owncast_get_status`.
- **owncast-viewers** (`OWNCAST_URL`): holds Viewer; read with `owncast_get_active_viewers`.
- **owncast-hardware** (`OWNCAST_URL`): holds HardwareSample; read with `owncast_get_hardware_stats`.
- **owncast-chat** (`OWNCAST_URL`): holds ChatMessage; read with `owncast_get_chat_messages_admin`.
- **owncast-followers** (`OWNCAST_URL`): holds Person; read with `owncast_get_followers`.

## Workflows (tool-use contracts)

Each workflow is a tool-use contract in the connector ontology. Run the steps in order; read before you write.

### `owncast-manage-ban`

1. `owncast_get_ipaddress_bans` (no parameters) - Get ipaddress bans.
2. `owncast_ban_ipaddress` (`body`) - Run ban ipaddress.
3. `owncast_unban_ipaddress` (`body`) - Run unban ipaddress.

### `owncast-manage-emoji`

1. `owncast_get_custom_emoji_list` (no parameters) - Get custom emoji list.
2. `owncast_upload_custom_emoji` (`data`, `name`) - Upload custom emoji.
3. `owncast_delete_custom_emoji` (`confirm`, `name`) - Delete custom emoji. (destructive: ask the operator first)

### `owncast-manage-message`

1. `owncast_external_get_chat_messages` (no parameters) - Run external get chat messages.
2. `owncast_get_chat_messages` (`access_token`) - Get chat messages.
3. `owncast_get_chat_messages_admin` (no parameters) - Get chat messages admin.
4. `owncast_send_chat_action` (`body`) - Send chat action.
5. `owncast_send_federated_message` (`body`) - Send federated message.
6. `owncast_send_integration_chat_message` (`body`) - Send integration chat message.
7. `owncast_send_system_message` (`body`) - Send system message.
8. `owncast_send_system_message_to_connected_client` (`body`, `client_id`) - Send system message to connected client.
9. `owncast_send_user_message` (no parameters) - Send user message.
10. `owncast_external_update_message_visibility` (`body`) - Run external update message visibility.
11. `owncast_update_message_visibility` (`access_token`, `body`) - Update message visibility.
12. `owncast_update_message_visibility_admin` (`body`) - Update message visibility admin.

### `owncast-manage-user`

1. `owncast_external_get_connected_chat_clients` (no parameters) - Run external get connected chat clients.
2. `owncast_external_get_user_details` (`user_id`) - Run external get user details.
3. `owncast_get_connected_chat_clients` (no parameters) - Get connected chat clients.
4. `owncast_get_disabled_users` (no parameters) - Get disabled users.
5. `owncast_get_moderators` (no parameters) - Get moderators.
6. `owncast_get_user_details` (`access_token`, `user_id`) - Get user details.
7. `owncast_register_anonymous_chat_user` (`display_name`, `x_forwarded_user`) - Register anonymous chat user.
8. `owncast_set_enable_established_chat_user_mode` (`body`) - Set enable established chat user mode.
9. `owncast_set_forbidden_username_list` (`value`) - Set forbidden username list.
10. `owncast_set_suggested_username_list` (`value`) - Set suggested username list.
11. `owncast_update_user_enabled` (`access_token`, `enabled`, `user_id`) - Update user enabled.
12. `owncast_update_user_enabled_admin` (`enabled`, `user_id`) - Update user enabled admin.
13. `owncast_update_user_moderator` (`is_moderator`, `user_id`) - Update user moderator.

### `owncast-manage-notification`

1. `owncast_register_for_live_notifications` (`access_token`, `channel`, `destination`) - Register for live notifications.

### `owncast-manage-chat-settings`

1. `owncast_set_chat_disabled` (`body`) - Set chat disabled.
2. `owncast_set_chat_join_messages_enabled` (`body`) - Set chat join messages enabled.
3. `owncast_set_chat_require_authentication` (`body`) - Set chat require authentication.
4. `owncast_set_chat_slur_filter_enabled` (`body`) - Set chat slur filter enabled.
5. `owncast_set_chat_spam_protection_enabled` (`body`) - Set chat spam protection enabled.

## Guardrails

- Never print or log the admin token, stream keys or webhook secrets.
- Read before you write: every change starts from the read steps of its contract.
- Confirm the stream is online before acting on live-only signals.
- Report a tool refusal or HTTP error as it is; never retry past a refusal or invent a result.
