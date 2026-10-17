
import pytest

import owncast_agent
import owncast_agent.mcp_server
from owncast_agent import __dir__


@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
def test_import_owncast_agent():
    """Test that the package imports successfully and exposes its interface.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    assert owncast_agent.__all__ is not None
    assert "OwncastApi" in owncast_agent.__all__




@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
def test_getattr_optional_module_success():
    """Test getattr loads and delegates optional module attributes successfully.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    func = owncast_agent.mcp_server
    assert func is not None
    assert callable(func)


@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
def test_getattr_attribute_error():
    """Test that requesting a non-existent attribute raises AttributeError.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    with pytest.raises(AttributeError):
        _ = owncast_agent.non_existent_attribute_xyz






@pytest.mark.concept("AU-ECO.mcp.fastmcp-middleware")
def test_dir_implementation():
    """Verify that __dir__ returns a sorted list of globals and __all__ elements.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    dir_list = __dir__()
    assert isinstance(dir_list, list)
    assert len(dir_list) > 0
    assert "OwncastApi" in dir_list
    assert dir_list == sorted(dir_list)
