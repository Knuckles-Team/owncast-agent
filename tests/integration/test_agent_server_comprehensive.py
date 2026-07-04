import importlib
import os
from unittest.mock import MagicMock, patch

import agent_utilities
import pytest

# 1. Directly inject mocks into the module dictionary to bypass dynamic __getattr__ lazy-loading
mock_init = MagicMock()
mock_load = MagicMock(
    return_value={
        "name": "Mock Owncast Agent",
        "description": "Mock Agent Description",
        "content": "Mock Agent System Prompt",
    }
)
mock_build = MagicMock(return_value="Mock Built System Prompt")

agent_utilities.__dict__["initialize_workspace"] = mock_init
agent_utilities.__dict__["load_identity"] = mock_load
agent_utilities.__dict__["build_system_prompt_from_workspace"] = mock_build

# Import the module to be tested
import owncast_agent.agent_server as agent_server

# Force-reload with os.environ keys explicitly cleared/mocked to ensure no environment pollution overrides meta values
with patch.dict(os.environ, {}, clear=True):
    importlib.reload(agent_server)


@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
def test_module_level_variables_on_import():
    """Verify module-level variables are correctly loaded and fallback logic is executed.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    assert mock_init.called
    assert mock_load.called
    assert agent_server.DEFAULT_AGENT_NAME == "Mock Owncast Agent"
    assert agent_server.DEFAULT_AGENT_DESCRIPTION == "Mock Agent Description"
    assert agent_server.DEFAULT_AGENT_SYSTEM_PROMPT == "Mock Agent System Prompt"


@pytest.mark.concept("AU-ORCH.adapter.kg-graph-materialization")
def test_agent_server_cli_execution():
    """Verify CLI configuration and server startup transitions with patched arguments.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    mock_parser = MagicMock()
    mock_args = MagicMock()

    # Configure mock arguments
    mock_args.mcp_url = "http://localhost:8000"
    mock_args.mcp_config = "custom_mcp_config.json"
    mock_args.host = "127.0.0.1"
    mock_args.port = 5000
    mock_args.provider = "openai"
    mock_args.model_id = "gpt-4"
    mock_args.base_url = "http://openai.api"
    mock_args.api_key = "secret-key"
    mock_args.custom_skills_directory = "./skills"
    mock_args.web = True
    mock_args.otel = False
    mock_args.otel_endpoint = None
    mock_args.otel_headers = None
    mock_args.otel_public_key = None
    mock_args.otel_secret_key = None
    mock_args.otel_protocol = None
    mock_args.debug = True

    mock_parser.parse_args.return_value = mock_args

    # Patch in the owncast_agent.agent_server namespace
    with (
        patch(
            "owncast_agent.agent_server.create_agent_parser", return_value=mock_parser
        ) as mock_create_parser,
        patch("owncast_agent.agent_server.create_agent_server") as mock_create_server,
        patch("sys.argv", ["agent_server.py"]),
    ):
        agent_server.agent_server()

        # Check create_agent_parser was called
        mock_create_parser.assert_called_once()

        # Check create_agent_server was called with the correct parameters
        mock_create_server.assert_called_once_with(
            mcp_url="http://localhost:8000",
            mcp_config="custom_mcp_config.json",
            host="127.0.0.1",
            port=5000,
            provider="openai",
            model_id="gpt-4",
            router_model="gpt-4",
            agent_model="gpt-4",
            base_url="http://openai.api",
            api_key="secret-key",
            custom_skills_directory="./skills",
            enable_web_ui=True,
            enable_otel=False,
            otel_endpoint=None,
            otel_headers=None,
            otel_public_key=None,
            otel_secret_key=None,
            otel_protocol=None,
            debug=True,
        )


@pytest.mark.concept("AU-ORCH.adapter.kg-graph-materialization")
def test_agent_server_main_execution():
    """Verify that calling the module directly runs the server.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    import runpy

    mock_parser = MagicMock()
    mock_args = MagicMock()
    mock_args.debug = False
    mock_parser.parse_args.return_value = mock_args

    with (
        patch("sys.argv", ["agent_server.py"]),
        patch(
            "agent_utilities.create_agent_parser", return_value=mock_parser
        ) as mock_create_parser,
        patch("agent_utilities.create_agent_server") as mock_create_server,
    ):
        runpy.run_module("owncast_agent.agent_server", run_name="__main__")

        mock_create_parser.assert_called_once()
        mock_create_server.assert_called_once()


@pytest.mark.concept("AU-ORCH.adapter.kg-graph-materialization")
def test_main_execution():
    """Verify that importing/running __main__ executes the server.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    import runpy

    with patch("owncast_agent.agent_server.agent_server") as mock_agent_server:
        runpy.run_module("owncast_agent.__main__", run_name="__main__")
        mock_agent_server.assert_called_once()
