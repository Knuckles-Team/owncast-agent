import importlib
from unittest.mock import patch

import pytest

import owncast_agent
import owncast_agent.mcp_server
from owncast_agent import __dir__


@pytest.mark.concept("ECO-4.1")
def test_import_owncast_agent():
    """Test that the package imports successfully and exposes its interface.

    CONCEPT:ECO-4.1
    """
    assert owncast_agent.__all__ is not None
    assert "OwncastApi" in owncast_agent.__all__


@pytest.mark.concept("ECO-4.1")
def test_getattr_mcp_agent_availability():
    """Test dynamic attribute checking for _MCP_AVAILABLE and _AGENT_AVAILABLE.

    CONCEPT:ECO-4.1
    """
    assert owncast_agent._MCP_AVAILABLE is True
    assert owncast_agent._AGENT_AVAILABLE is True


@pytest.mark.concept("ECO-4.1")
def test_getattr_optional_module_success():
    """Test getattr loads and delegates optional module attributes successfully.

    CONCEPT:ECO-4.1
    """
    func = owncast_agent.mcp_server
    assert func is not None
    assert callable(func)


@pytest.mark.concept("ECO-4.1")
def test_getattr_attribute_error():
    """Test that requesting a non-existent attribute raises AttributeError.

    CONCEPT:ECO-4.1
    """
    with pytest.raises(AttributeError):
        _ = owncast_agent.non_existent_attribute_xyz


@pytest.mark.concept("ECO-4.1")
def test_getattr_import_error_simulation():
    """Simulate module import failures to cover the except ImportError blocks.

    CONCEPT:ECO-4.1
    """
    import owncast_agent as oa

    oa._loaded_optional_modules.clear()

    original_import = importlib.import_module

    def mock_import(name, *args, **kwargs):
        if name in oa.OPTIONAL_MODULES:
            raise ImportError(f"Simulated import error for {name}")
        return original_import(name, *args, **kwargs)

    with patch("importlib.import_module", side_effect=mock_import):
        assert oa.__getattr__("_MCP_AVAILABLE") is False
        assert oa.__getattr__("_AGENT_AVAILABLE") is False

        with pytest.raises(AttributeError):
            _ = oa.__getattr__("mcp_server")


@pytest.mark.concept("ECO-4.1")
def test_getattr_availability_fallback():
    """Verify fallback return False when OPTIONAL_MODULES keys are missing.

    CONCEPT:ECO-4.1
    """
    import owncast_agent as oa

    with patch.dict(oa.OPTIONAL_MODULES, {}, clear=True):
        assert oa.__getattr__("_MCP_AVAILABLE") is False
        assert oa.__getattr__("_AGENT_AVAILABLE") is False


@pytest.mark.concept("ECO-4.1")
def test_dir_implementation():
    """Verify that __dir__ returns a sorted list of globals and __all__ elements.

    CONCEPT:ECO-4.1
    """
    dir_list = __dir__()
    assert isinstance(dir_list, list)
    assert len(dir_list) > 0
    assert "OwncastApi" in dir_list
    assert dir_list == sorted(dir_list)
