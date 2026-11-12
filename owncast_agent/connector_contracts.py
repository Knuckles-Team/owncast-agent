"""Surface contracts: tool use, links, data locations and business roles."""

from scion_sdk.surface_contracts import (
    BusinessRole,
    DataLocation,
    Refusal,
    SurfaceLink,
    ToolStep,
    ToolUseContract,
)

CONTRACTS = (
    ToolUseContract(
        "owncast-manage-maintenance",
        (
            ToolStep(
                "owncast_auto_update_force_quit",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_auto_update_options",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_auto_update_start",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-broadcast",
        (
            ToolStep(
                "owncast_get_status",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_ping",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_status_admin",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_disconnect_inbound_connection",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_stream_title",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-inspect-viewers",
        (
            ToolStep(
                "owncast_get_active_viewers",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_viewers_over_time",
                params=(
                    "window_start",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-inspect-hardware",
        (
            ToolStep(
                "owncast_get_hardware_stats",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-diagnostics",
        (
            ToolStep(
                "owncast_get_logs",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_warnings",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_ypresponse",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_reset_ypregistration",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                    Refusal("CONFIRMATION_REQUIRED", "the caller has not confirmed the destructive call"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-playback",
        (
            ToolStep(
                "owncast_get_video_playback_metrics",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_video_stream_output_variants",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_report_playback_metrics",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_stream_output_variants",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-telemetry",
        (
            ToolStep(
                "owncast_ingest_telemetry",
                params=(
                    "access_token",
                    "include",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-ban",
        (
            ToolStep(
                "owncast_get_ipaddress_bans",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_ban_ipaddress",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_unban_ipaddress",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-emoji",
        (
            ToolStep(
                "owncast_get_custom_emoji_list",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_upload_custom_emoji",
                params=(
                    "data",
                    "name",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_delete_custom_emoji",
                params=(
                    "confirm",
                    "name",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                    Refusal("CONFIRMATION_REQUIRED", "the caller has not confirmed the destructive call"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-message",
        (
            ToolStep(
                "owncast_external_get_chat_messages",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_chat_messages",
                params=(
                    "access_token",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_chat_messages_admin",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_send_chat_action",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_send_federated_message",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_send_integration_chat_message",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_send_system_message",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_send_system_message_to_connected_client",
                params=(
                    "body",
                    "client_id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_send_user_message",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_external_update_message_visibility",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_update_message_visibility",
                params=(
                    "access_token",
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_update_message_visibility_admin",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-user",
        (
            ToolStep(
                "owncast_external_get_connected_chat_clients",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_external_get_user_details",
                params=(
                    "user_id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_connected_chat_clients",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_disabled_users",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_moderators",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_user_details",
                params=(
                    "access_token",
                    "user_id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_register_anonymous_chat_user",
                params=(
                    "display_name",
                    "x_forwarded_user",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_enable_established_chat_user_mode",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_forbidden_username_list",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_suggested_username_list",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_update_user_enabled",
                params=(
                    "access_token",
                    "enabled",
                    "user_id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_update_user_enabled_admin",
                params=(
                    "enabled",
                    "user_id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_update_user_moderator",
                params=(
                    "is_moderator",
                    "user_id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-notification",
        (
            ToolStep(
                "owncast_register_for_live_notifications",
                params=(
                    "access_token",
                    "channel",
                    "destination",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-chat-settings",
        (
            ToolStep(
                "owncast_set_chat_disabled",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_chat_join_messages_enabled",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_chat_require_authentication",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_chat_slur_filter_enabled",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_chat_spam_protection_enabled",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-follower",
        (
            ToolStep(
                "owncast_get_blocked_and_rejected_followers",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_followers",
                params=(
                    "limit",
                    "offset",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_followers_admin",
                params=(
                    "limit",
                    "offset",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_pending_follow_requests",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_approve_follower",
                params=(
                    "actor_iri",
                    "approved",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_remote_follow",
                params=(
                    "account",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-inspect-federated-message",
        (
            ToolStep(
                "owncast_get_federated_actions",
                params=(
                    "limit",
                    "offset",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-fediverse-auth",
        (
            ToolStep(
                "owncast_register_fediverse_otprequest",
                params=(
                    "access_token",
                    "account",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_verify_fediverse_otprequest",
                params=(
                    "code",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-federation-settings",
        (
            ToolStep(
                "owncast_set_federation_activity_private",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_federation_block_domains",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_federation_enabled",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_federation_go_live_message",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_federation_show_engagement",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_federation_username",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-api-user",
        (
            ToolStep(
                "owncast_get_external_apiusers",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_create_external_apiuser",
                params=(
                    "name",
                    "scopes",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_delete_external_apiuser",
                params=(
                    "confirm",
                    "token",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                    Refusal("CONFIRMATION_REQUIRED", "the caller has not confirmed the destructive call"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-webhook",
        (
            ToolStep(
                "owncast_get_webhooks",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_create_webhook",
                params=(
                    "events",
                    "url",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_delete_webhook",
                params=(
                    "confirm",
                    "id",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                    Refusal("CONFIRMATION_REQUIRED", "the caller has not confirmed the destructive call"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-prometheus",
        (
            ToolStep(
                "owncast_get_prometheus_api",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_post_prometheus_api",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_put_prometheus_api",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_delete_prometheus_api",
                params=(
                    "confirm",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                    Refusal("CONFIRMATION_REQUIRED", "the caller has not confirmed the destructive call"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-external-api",
        (
            ToolStep(
                "owncast_external_get_status",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_external_set_stream_title",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-indie-auth",
        (
            ToolStep(
                "owncast_start_indie_auth_flow",
                params=(
                    "access_token",
                    "auth_host",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_handle_indie_auth_endpoint_get",
                params=(
                    "client_id",
                    "code_challenge",
                    "redirect_uri",
                    "state",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_handle_indie_auth_endpoint_post",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_handle_indie_auth_redirect",
                params=(
                    "state",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-inspect-config",
        (
            ToolStep(
                "owncast_get_all_social_platforms",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_server_config",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
            ToolStep(
                "owncast_get_web_config",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("NOT_FOUND", "the requested record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-appearance",
        (
            ToolStep(
                "owncast_set_custom_color_variable_values",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_custom_javascript",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_custom_offline_message",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_custom_styles",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_external_actions",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_extra_page_content",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_favicon",
                params=(),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_logo",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_reset_favicon",
                params=(
                    "confirm",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                    Refusal("CONFIRMATION_REQUIRED", "the caller has not confirmed the destructive call"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-identity",
        (
            ToolStep(
                "owncast_set_admin_password",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_directory_enabled",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_disable_search_indexing",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_hide_viewer_count",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_nsfw",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_server_name",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_server_summary",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_server_url",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_server_welcome_message",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_social_handles",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-notifications",
        (
            ToolStep(
                "owncast_set_browser_notification_configuration",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_discord_notification_configuration",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "owncast-manage-video",
        (
            ToolStep(
                "owncast_set_ffmpeg_path",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_rtmpserver_port",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_s3_configuration",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_socket_host_override",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_stream_keys",
                params=(
                    "value",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_stream_latency_level",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_tags",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_video_codec",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_video_serving_endpoint",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_web_server_ip",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
            ToolStep(
                "owncast_set_web_server_port",
                params=(
                    "body",
                ),
                result=(
                    "result",
                ),
                refusals=(
                    Refusal("ACCESS_DENIED", "the credential lacks access to the operation"),
                    Refusal("INVALID_ARGUMENT", "the upstream system rejects the input"),
                ),
            ),
        ),
    ),
)

LINKS = (
    SurfaceLink(
        "owncast-manage-maintenance",
        tools=(
            "owncast_auto_update_force_quit",
            "owncast_auto_update_options",
            "owncast_auto_update_start",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-stream-health",
        ),
    ),
    SurfaceLink(
        "owncast-manage-broadcast",
        tools=(
            "owncast_disconnect_inbound_connection",
            "owncast_get_status",
            "owncast_ping",
            "owncast_set_stream_title",
            "owncast_status_admin",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-stream-health",
        ),
    ),
    SurfaceLink(
        "owncast-inspect-viewers",
        tools=(
            "owncast_get_active_viewers",
            "owncast_get_viewers_over_time",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-stream-health",
        ),
    ),
    SurfaceLink(
        "owncast-inspect-hardware",
        tools=(
            "owncast_get_hardware_stats",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-stream-health",
        ),
    ),
    SurfaceLink(
        "owncast-manage-diagnostics",
        tools=(
            "owncast_get_logs",
            "owncast_get_warnings",
            "owncast_get_ypresponse",
            "owncast_reset_ypregistration",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-stream-health",
        ),
    ),
    SurfaceLink(
        "owncast-manage-playback",
        tools=(
            "owncast_get_video_playback_metrics",
            "owncast_get_video_stream_output_variants",
            "owncast_report_playback_metrics",
            "owncast_set_stream_output_variants",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-stream-health",
        ),
    ),
    SurfaceLink(
        "owncast-manage-telemetry",
        tools=(
            "owncast_ingest_telemetry",
        ),
        prompts=(
            "owncast-stream-operator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-audience-ingestion",
        ),
    ),
    SurfaceLink(
        "owncast-manage-ban",
        tools=(
            "owncast_ban_ipaddress",
            "owncast_get_ipaddress_bans",
            "owncast_unban_ipaddress",
        ),
        prompts=(
            "owncast-chat-moderator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-administration",
        ),
    ),
    SurfaceLink(
        "owncast-manage-emoji",
        tools=(
            "owncast_delete_custom_emoji",
            "owncast_get_custom_emoji_list",
            "owncast_upload_custom_emoji",
        ),
        prompts=(
            "owncast-chat-moderator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-administration",
        ),
    ),
    SurfaceLink(
        "owncast-manage-message",
        tools=(
            "owncast_external_get_chat_messages",
            "owncast_external_update_message_visibility",
            "owncast_get_chat_messages",
            "owncast_get_chat_messages_admin",
            "owncast_send_chat_action",
            "owncast_send_federated_message",
            "owncast_send_integration_chat_message",
            "owncast_send_system_message",
            "owncast_send_system_message_to_connected_client",
            "owncast_send_user_message",
            "owncast_update_message_visibility",
            "owncast_update_message_visibility_admin",
        ),
        prompts=(
            "owncast-chat-moderator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-administration",
        ),
    ),
    SurfaceLink(
        "owncast-manage-user",
        tools=(
            "owncast_external_get_connected_chat_clients",
            "owncast_external_get_user_details",
            "owncast_get_connected_chat_clients",
            "owncast_get_disabled_users",
            "owncast_get_moderators",
            "owncast_get_user_details",
            "owncast_register_anonymous_chat_user",
            "owncast_set_enable_established_chat_user_mode",
            "owncast_set_forbidden_username_list",
            "owncast_set_suggested_username_list",
            "owncast_update_user_enabled",
            "owncast_update_user_enabled_admin",
            "owncast_update_user_moderator",
        ),
        prompts=(
            "owncast-chat-moderator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-administration",
        ),
    ),
    SurfaceLink(
        "owncast-manage-notification",
        tools=(
            "owncast_register_for_live_notifications",
        ),
        prompts=(
            "owncast-chat-moderator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-administration",
        ),
    ),
    SurfaceLink(
        "owncast-manage-chat-settings",
        tools=(
            "owncast_set_chat_disabled",
            "owncast_set_chat_join_messages_enabled",
            "owncast_set_chat_require_authentication",
            "owncast_set_chat_slur_filter_enabled",
            "owncast_set_chat_spam_protection_enabled",
        ),
        prompts=(
            "owncast-chat-moderator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-administration",
        ),
    ),
    SurfaceLink(
        "owncast-manage-follower",
        tools=(
            "owncast_approve_follower",
            "owncast_get_blocked_and_rejected_followers",
            "owncast_get_followers",
            "owncast_get_followers_admin",
            "owncast_get_pending_follow_requests",
            "owncast_remote_follow",
        ),
        prompts=(
            "owncast-community-manager",
            "streaming_specialist",
        ),
        skills=(
            "owncast-federation",
        ),
    ),
    SurfaceLink(
        "owncast-inspect-federated-message",
        tools=(
            "owncast_get_federated_actions",
        ),
        prompts=(
            "owncast-community-manager",
            "streaming_specialist",
        ),
        skills=(
            "owncast-federation",
        ),
    ),
    SurfaceLink(
        "owncast-manage-fediverse-auth",
        tools=(
            "owncast_register_fediverse_otprequest",
            "owncast_verify_fediverse_otprequest",
        ),
        prompts=(
            "owncast-community-manager",
            "streaming_specialist",
        ),
        skills=(
            "owncast-federation",
        ),
    ),
    SurfaceLink(
        "owncast-manage-federation-settings",
        tools=(
            "owncast_set_federation_activity_private",
            "owncast_set_federation_block_domains",
            "owncast_set_federation_enabled",
            "owncast_set_federation_go_live_message",
            "owncast_set_federation_show_engagement",
            "owncast_set_federation_username",
        ),
        prompts=(
            "owncast-community-manager",
            "streaming_specialist",
        ),
        skills=(
            "owncast-federation",
        ),
    ),
    SurfaceLink(
        "owncast-manage-api-user",
        tools=(
            "owncast_create_external_apiuser",
            "owncast_delete_external_apiuser",
            "owncast_get_external_apiusers",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-integrations",
        ),
    ),
    SurfaceLink(
        "owncast-manage-webhook",
        tools=(
            "owncast_create_webhook",
            "owncast_delete_webhook",
            "owncast_get_webhooks",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-integrations",
        ),
    ),
    SurfaceLink(
        "owncast-manage-prometheus",
        tools=(
            "owncast_delete_prometheus_api",
            "owncast_get_prometheus_api",
            "owncast_post_prometheus_api",
            "owncast_put_prometheus_api",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-integrations",
        ),
    ),
    SurfaceLink(
        "owncast-manage-external-api",
        tools=(
            "owncast_external_get_status",
            "owncast_external_set_stream_title",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-integrations",
        ),
    ),
    SurfaceLink(
        "owncast-manage-indie-auth",
        tools=(
            "owncast_handle_indie_auth_endpoint_get",
            "owncast_handle_indie_auth_endpoint_post",
            "owncast_handle_indie_auth_redirect",
            "owncast_start_indie_auth_flow",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-integrations",
        ),
    ),
    SurfaceLink(
        "owncast-inspect-config",
        tools=(
            "owncast_get_all_social_platforms",
            "owncast_get_server_config",
            "owncast_get_web_config",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-server-settings",
        ),
    ),
    SurfaceLink(
        "owncast-manage-appearance",
        tools=(
            "owncast_reset_favicon",
            "owncast_set_custom_color_variable_values",
            "owncast_set_custom_javascript",
            "owncast_set_custom_offline_message",
            "owncast_set_custom_styles",
            "owncast_set_external_actions",
            "owncast_set_extra_page_content",
            "owncast_set_favicon",
            "owncast_set_logo",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-server-settings",
        ),
    ),
    SurfaceLink(
        "owncast-manage-identity",
        tools=(
            "owncast_set_admin_password",
            "owncast_set_directory_enabled",
            "owncast_set_disable_search_indexing",
            "owncast_set_hide_viewer_count",
            "owncast_set_nsfw",
            "owncast_set_server_name",
            "owncast_set_server_summary",
            "owncast_set_server_url",
            "owncast_set_server_welcome_message",
            "owncast_set_social_handles",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-server-settings",
        ),
    ),
    SurfaceLink(
        "owncast-manage-notifications",
        tools=(
            "owncast_set_browser_notification_configuration",
            "owncast_set_discord_notification_configuration",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-server-settings",
        ),
    ),
    SurfaceLink(
        "owncast-manage-video",
        tools=(
            "owncast_set_ffmpeg_path",
            "owncast_set_rtmpserver_port",
            "owncast_set_s3_configuration",
            "owncast_set_socket_host_override",
            "owncast_set_stream_keys",
            "owncast_set_stream_latency_level",
            "owncast_set_tags",
            "owncast_set_video_codec",
            "owncast_set_video_serving_endpoint",
            "owncast_set_web_server_ip",
            "owncast_set_web_server_port",
        ),
        prompts=(
            "owncast-site-administrator",
            "streaming_specialist",
        ),
        skills=(
            "owncast-server-settings",
        ),
    ),
    SurfaceLink(
        "owncast-agent-operations",
        tools=(
            "owncast_get_status",
            "owncast_ping",
        ),
        prompts=(
            "streaming_specialist",
        ),
        skills=(
            "owncast-agent-operations",
        ),
    ),
    SurfaceLink(
        "owncast-audience-ingestion",
        tools=(
            "owncast_ingest_telemetry",
        ),
        prompts=(
            "streaming_specialist",
        ),
        skills=(
            "owncast-audience-ingestion",
        ),
    ),
    SurfaceLink(
        "owncast-broadcast-monitoring",
        tools=(
            "owncast_disconnect_inbound_connection",
            "owncast_get_active_viewers",
            "owncast_get_hardware_stats",
            "owncast_get_status",
            "owncast_get_viewers_over_time",
            "owncast_ingest_telemetry",
            "owncast_status_admin",
        ),
        prompts=(
            "streaming_specialist",
        ),
        skills=(
            "owncast-broadcast-monitoring",
        ),
    ),
    SurfaceLink(
        "owncast-chat-moderation",
        tools=(
            "owncast_ban_ipaddress",
            "owncast_get_chat_messages",
            "owncast_get_chat_messages_admin",
            "owncast_get_connected_chat_clients",
            "owncast_get_disabled_users",
            "owncast_get_ipaddress_bans",
            "owncast_get_moderators",
            "owncast_unban_ipaddress",
            "owncast_update_message_visibility_admin",
            "owncast_update_user_enabled_admin",
            "owncast_update_user_moderator",
        ),
        prompts=(
            "streaming_specialist",
        ),
        skills=(
            "owncast-chat-moderation",
        ),
    ),
)

LOCATIONS = (
    DataLocation(
        "owncast-stream",
        (
            "Stream",
        ),
        "OWNCAST_URL",
        "owncast_get_status",
    ),
    DataLocation(
        "owncast-viewers",
        (
            "Viewer",
        ),
        "OWNCAST_URL",
        "owncast_get_active_viewers",
    ),
    DataLocation(
        "owncast-hardware",
        (
            "HardwareSample",
        ),
        "OWNCAST_URL",
        "owncast_get_hardware_stats",
    ),
    DataLocation(
        "owncast-chat",
        (
            "ChatMessage",
        ),
        "OWNCAST_URL",
        "owncast_get_chat_messages_admin",
    ),
    DataLocation(
        "owncast-followers",
        (
            "Person",
        ),
        "OWNCAST_URL",
        "owncast_get_followers",
    ),
)

ROLES = (
    BusinessRole(
        "stream operator",
        tasks=(
            "owncast-inspect-hardware",
            "owncast-inspect-viewers",
            "owncast-manage-broadcast",
            "owncast-manage-diagnostics",
            "owncast-manage-maintenance",
            "owncast-manage-playback",
            "owncast-manage-telemetry",
        ),
    ),
    BusinessRole(
        "chat moderator",
        tasks=(
            "owncast-manage-ban",
            "owncast-manage-chat-settings",
            "owncast-manage-emoji",
            "owncast-manage-message",
            "owncast-manage-notification",
            "owncast-manage-user",
        ),
    ),
    BusinessRole(
        "community manager",
        tasks=(
            "owncast-inspect-federated-message",
            "owncast-manage-federation-settings",
            "owncast-manage-fediverse-auth",
            "owncast-manage-follower",
        ),
    ),
    BusinessRole(
        "site administrator",
        tasks=(
            "owncast-inspect-config",
            "owncast-manage-api-user",
            "owncast-manage-appearance",
            "owncast-manage-external-api",
            "owncast-manage-identity",
            "owncast-manage-indie-auth",
            "owncast-manage-notifications",
            "owncast-manage-prometheus",
            "owncast-manage-video",
            "owncast-manage-webhook",
        ),
    ),
)
