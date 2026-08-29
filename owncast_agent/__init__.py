#!/usr/bin/env python

import importlib
import inspect
from typing import Any

__all__: list[str] = []

CORE_MODULES: list[str] = ["owncast_agent.api_client"]

OPTIONAL_MODULES = {
    "owncast_agent.agent_server": "agent",
    "owncast_agent.mcp_server": "mcp",
}


def _expose_members(module):
    """Expose public classes and functions from a module into globals and __all__."""
    for name, obj in inspect.getmembers(module):
        if (inspect.isclass(obj) or inspect.isfunction(obj)) and not name.startswith(
            "_"
        ):
            globals()[name] = obj
            if name not in __all__:
                __all__.append(name)


# Eagerly import core modules (keeps API wrappers fast & light)
for module_name in CORE_MODULES:
    if module_name:
        module = importlib.import_module(module_name)
        _expose_members(module)

# Dynamic/lazy loading of optional modules (agent_server, mcp_server)
_loaded_optional_modules: dict[str, Any] = {}


def _import_module_safely(module_name: str):
    """Try to import a module and return it, or None if not available."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


# Marker substrings used to locate each availability flag's backing module in
# OPTIONAL_MODULES, keyed by the dunder-ish flag name callers probe for.
_AVAILABILITY_FLAG_MARKERS = {
    "_MCP_AVAILABLE": "mcp_server",
    "_AGENT_AVAILABLE": "agent_server",
}


def _resolve_availability_flag(name: str) -> bool | None:
    """Return an ``_*_AVAILABLE`` flag's live value, or None if ``name`` isn't one."""
    marker = _AVAILABILITY_FLAG_MARKERS.get(name)
    if marker is None:
        return None
    module_key = next((k for k in OPTIONAL_MODULES if marker in k), None)
    if module_key is None:
        return False
    return _import_module_safely(module_key) is not None


def _find_attr_in_optional_modules(name: str) -> Any:
    """Import (and cache) each optional module in turn, searching for ``name``."""
    for module_name in OPTIONAL_MODULES:
        if module_name not in _loaded_optional_modules:
            module = _import_module_safely(module_name)
            if module is not None:
                _loaded_optional_modules[module_name] = module
                _expose_members(module)

        module = _loaded_optional_modules.get(module_name)
        if module is not None and hasattr(module, name):
            return getattr(module, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __getattr__(name: str) -> Any:
    """Dynamic attribute access for lazy loading optional modules.

    CONCEPT:AU-ORCH.adapter.kg-graph-materialization
    """
    flag_value = _resolve_availability_flag(name)
    if flag_value is not None:
        return flag_value
    return _find_attr_in_optional_modules(name)


def __dir__() -> list[str]:
    return sorted(list(globals().keys()) + __all__)
