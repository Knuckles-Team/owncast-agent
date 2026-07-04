"""Tests for standardized action discovery via the shared helper.

CONCEPT:AU-ECO.mcp.fastmcp-middleware
"""

import pytest
from agent_utilities.mcp_utilities import resolve_action

from owncast_agent.mcp_server import (
    ALLOWED_CHAT_ACTIONS,
    ALLOWED_EXTERNAL_ACTIONS,
    ALLOWED_INTERNAL_ACTIONS,
    ALLOWED_OBJECTS_ACTIONS,
)

ALLOWED_SETS = [
    ALLOWED_INTERNAL_ACTIONS,
    ALLOWED_OBJECTS_ACTIONS,
    ALLOWED_EXTERNAL_ACTIONS,
    ALLOWED_CHAT_ACTIONS,
]


@pytest.mark.parametrize("allowed", ALLOWED_SETS)
def test_list_actions_returns_names(allowed):
    """`list_actions` yields a discovery payload listing every valid action."""
    result = resolve_action("list_actions", allowed, service="owncast-agent")
    assert isinstance(result, dict)
    assert result["service"] == "owncast-agent"
    assert set(result["actions"]) == set(allowed)


@pytest.mark.parametrize("allowed", ALLOWED_SETS)
def test_bogus_action_raises_with_list_actions_hint(allowed):
    """An unknown action raises a rich error mentioning `list_actions`."""
    with pytest.raises(ValueError) as exc:
        resolve_action("definitely_not_a_real_action", allowed, service="owncast-agent")
    assert "list_actions" in str(exc.value)


def test_known_action_resolves_to_canonical():
    """A valid action passes through as its canonical string."""
    action = next(iter(ALLOWED_INTERNAL_ACTIONS))
    resolved = resolve_action(action, ALLOWED_INTERNAL_ACTIONS, service="owncast-agent")
    assert resolved == action
