#!/usr/bin/env python3
import ast
import glob
import os
import sys
from typing import TypeGuard

BASELINES = {
    "adguard-home-agent": 89.2,
    "ansible-tower-mcp": 94.7,
    "archivebox-api": 85.7,
    "documentdb-mcp": 100.0,
    "github-agent": 100.0,
    "gitlab-api": 6.4,
    "home-assistant-agent": 63.6,
    "jellyfin-mcp": 81.0,
    "langfuse-agent": 100.0,
    "listmonk-api": 87.5,
    "mealie-mcp": 96.4,
    "microsoft-agent": 99.6,
    "nextcloud-agent": 52.6,
    "owncast-agent": 100.0,
    "plane-agent": 54.9,
    "portainer-agent": 35.5,
    "postiz-agent": 0.0,
    "qbittorrent-agent": 70.8,
    "scholarx": 90.0,
    "servicenow-api": 73.1,
    "stirlingpdf-agent": 0.0,
    "wger-agent": 41.7,
}


def _looks_like_api_client_class(node: ast.ClassDef) -> bool:
    """True for a class named like an API/Client wrapper (``Api``, ``*Api``, ``*Client``)."""
    class_name = node.name.lower()
    return "api" in class_name or "client" in class_name or node.name == "Api"


def _is_public_client_method(
    item: ast.stmt,
) -> TypeGuard[ast.FunctionDef | ast.AsyncFunctionDef]:
    """True for a public (non-private, non-``authenticate``) method definition."""
    if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return False
    return not item.name.startswith("_") and item.name != "authenticate"


def _public_methods_of_class(node: ast.ClassDef) -> dict:
    """Collect ``{method_name: {line, class}}`` for one class's own public methods.

    Only methods defined directly in the class body are seen -- inherited methods
    (e.g. a composed ``class Api(MixinA, MixinB): pass``) are not resolved here.
    """
    return {
        item.name: {"line": item.lineno, "class": node.name}
        for item in node.body
        if _is_public_client_method(item)
    }


def parse_api_client(filepath):
    """Parses api_client.py to find the main API/Client class and its public methods.

    Returns a set of method names.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=filepath)

    methods = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and _looks_like_api_client_class(node):
            methods.update(_public_methods_of_class(node))
    return methods


class MethodCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.called_methods = set()
        self.action_literals = set()

    def visit_Attribute(self, node):
        # E.g. client.get_repositories
        if isinstance(node.value, ast.Name):
            # Typically client, api, self
            if node.value.id in ("client", "api", "self"):
                self.called_methods.add(node.attr)
        self.generic_visit(node)

    def visit_Call(self, node):
        # E.g. getattr(client, "foo")
        if isinstance(node.func, ast.Name) and node.func.id == "getattr":
            if len(node.args) >= 2 and isinstance(node.args[0], ast.Name):
                if node.args[0].id in ("client", "api"):
                    if isinstance(node.args[1], ast.Constant):
                        self.called_methods.add(node.args[1].value)
        self.generic_visit(node)

    def visit_Compare(self, node):
        # Capture action comparisons, e.g. action == "get"
        for op, comparator in zip(node.ops, node.comparators, strict=True):
            if isinstance(op, (ast.Eq, ast.In)):
                if isinstance(comparator, ast.Constant) and isinstance(
                    comparator.value, str
                ):
                    self.action_literals.add(comparator.value)
        self.generic_visit(node)


_TOOL_NAME_PREFIXES = ("github_", "gitlab_", "adguard_", "atlassian_")


def _decorator_marks_tool(dec: ast.expr) -> bool:
    """True for a decorator that is (or calls) something whose attribute is ``tool``."""
    target = dec.func if isinstance(dec, ast.Call) else dec
    return isinstance(target, ast.Attribute) and target.attr == "tool"


def _is_tool_function(node) -> bool:
    """True for an ``@mcp.tool``-decorated function, or a known tool-name-prefixed one."""
    if any(_decorator_marks_tool(dec) for dec in node.decorator_list):
        return True
    return node.name.startswith(_TOOL_NAME_PREFIXES)


def _map_tool_function(node, api_methods):
    """Visit one tool function, returning its mapping entry plus the api methods it calls."""
    visitor = MethodCallVisitor()
    visitor.visit(node)
    mapped = visitor.called_methods.intersection(api_methods.keys())
    entry = {"methods": list(mapped), "actions": list(visitor.action_literals)}
    return entry, mapped


def parse_mcp_server(filepath, api_methods):
    """Parses mcp_server.py to extract registered tools and identify which api_methods they leverage.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=filepath)

    tool_mappings = {}
    all_mapped_methods = set()

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not _is_tool_function(node):
            continue
        entry, mapped = _map_tool_function(node, api_methods)
        tool_mappings[node.name] = entry
        all_mapped_methods.update(mapped)

    return tool_mappings, all_mapped_methods


def verify_agent(agent_dir):
    """Verify integration parity for a single agent.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    # Find api_client.py and mcp_server.py
    api_clients = glob.glob(
        os.path.join(agent_dir, "**", "api_client.py"), recursive=True
    )
    mcp_servers = glob.glob(
        os.path.join(agent_dir, "**", "mcp_server.py"), recursive=True
    )

    if not api_clients or not mcp_servers:
        return None

    api_client_path = api_clients[0]
    mcp_server_path = mcp_servers[0]

    api_methods = parse_api_client(api_client_path)
    if not api_methods:
        return None

    tool_mappings, mapped_methods = parse_mcp_server(mcp_server_path, api_methods)

    total_methods = len(api_methods)
    covered_methods = len(mapped_methods)
    coverage = (covered_methods / total_methods) * 100 if total_methods > 0 else 0.0

    unmapped = set(api_methods.keys()) - mapped_methods

    return {
        "agent_name": os.path.basename(agent_dir),
        "api_client": api_client_path,
        "mcp_server": mcp_server_path,
        "total_methods": total_methods,
        "covered_methods": covered_methods,
        "coverage": coverage,
        "unmapped": sorted(list(unmapped)),
        "mapped": sorted(list(mapped_methods)),
        "tool_mappings": tool_mappings,
    }


def _print_local_check(res: dict, baseline: float) -> bool:
    """Print the local single-agent parity report; return True iff it meets baseline."""
    agent_name = res["agent_name"]
    coverage = res["coverage"]

    print(f"=== API-to-MCP Integration Parity Check for: {agent_name} ===")
    print(f"- API client methods: {res['total_methods']}")
    print(f"- Integrated methods: {res['covered_methods']}")
    print(f"- Current Coverage  : {coverage:.1f}%")
    print(f"- Target Baseline   : {baseline:.1f}%")

    # Allow small floating point tolerance (0.05%)
    if coverage < (baseline - 0.05):
        print(
            f"\n❌ FAILED: Integration coverage ({coverage:.1f}%) has DEGRADED below the required baseline of {baseline:.1f}%!"
        )
        print(
            "Please ensure any new or refactored API client methods are properly integrated into MCP server tools."
        )
        if res["unmapped"]:
            print("\nUnmapped API methods:")
            for m in res["unmapped"]:
                print(f"  - {m}")
        return False

    print("\n✅ PASSED: Integration coverage meets or exceeds the required baseline!")
    return True


def _run_local_check():
    """Validate integration parity for the current-directory agent; exits the process."""
    res = verify_agent(os.getcwd())
    if not res:
        # If no client or server found in this dir, pass silently (e.g. non-python files, doc edits)
        print(
            "Skipping integration parity verification: No mcp_server.py/api_client.py found in current directory."
        )
        sys.exit(0)

    baseline = BASELINES.get(res["agent_name"], 0.0)
    passed = _print_local_check(res, baseline)
    sys.exit(0 if passed else 1)


def _discover_agent_dirs(agents_dir: str) -> list:
    """List candidate agent directories: top-level entries plus one nesting level."""
    agent_dirs = [
        d for d in glob.glob(os.path.join(agents_dir, "*")) if os.path.isdir(d)
    ]
    nested_dirs = [
        d for d in glob.glob(os.path.join(agents_dir, "*", "*")) if os.path.isdir(d)
    ]
    return sorted(set(agent_dirs + nested_dirs))


def _is_scannable_agent_dir(agent_dir: str) -> bool:
    """False for dotdirs, venvs, and egg-info dirs -- never a real agent package."""
    name = os.path.basename(agent_dir)
    return not (name.startswith(".") or "venv" in agent_dir or "egg-info" in agent_dir)


def _collect_agent_results(agent_dirs: list) -> list:
    """Run verify_agent over every scannable dir, skipping failures individually."""
    results = []
    for agent_dir in agent_dirs:
        if not _is_scannable_agent_dir(agent_dir):
            continue
        try:
            res = verify_agent(agent_dir)
        except Exception as e:
            print(f"Operation failed: {type(e).__name__}", file=sys.stderr)
            continue
        if res:
            results.append(res)
    return results


def _print_summary_table(results: list) -> None:
    print("| Agent Name | API Methods | Covered Methods | Coverage % | Status |")
    print("|---|---|---|---|---|")
    for r in results:
        status = "✅ 100%" if r["coverage"] >= 100.0 else "⚠️ Parity Gap"
        print(
            f"| {r['agent_name']} | {r['total_methods']} | {r['covered_methods']} | {r['coverage']:.1f}% | {status} |"
        )


def _print_agent_gap_detail(r: dict, agents_dir: str) -> None:
    if r["coverage"] < 100.0:
        print(f"### ⚠️ {r['agent_name']} ({r['coverage']:.1f}% Integration)")
        print(f"- **API Client**: `{os.path.relpath(r['api_client'], agents_dir)}`")
        print(f"- **MCP Server**: `{os.path.relpath(r['mcp_server'], agents_dir)}`")
        print("- **Unmapped API Methods**:")
        for m in r["unmapped"]:
            print(f"  - `{m}`")
        print()
    else:
        print(f"### ✅ {r['agent_name']} (100% Integration)")
        print(f"- All {r['total_methods']} methods successfully mapped to MCP tools.")
        print()


def _run_workspace_scan():
    """Scan every agent under the workspace and print the full parity report."""
    agents_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    agent_dirs = _discover_agent_dirs(agents_dir)
    results = _collect_agent_results(agent_dirs)

    print("# API to MCP Integration Parity Report")
    print(f"Scan Directory: `{agents_dir}`\n")
    _print_summary_table(results)
    print("\n## Detailed Parity Gaps\n")
    for r in results:
        _print_agent_gap_detail(r, agents_dir)


def main():
    """Main verification script entry point.

    CONCEPT:AU-ECO.mcp.fastmcp-middleware
    """
    args = sys.argv[1:]

    if "--local" in args or "--pre-commit" in args:
        _run_local_check()
        return

    _run_workspace_scan()


if __name__ == "__main__":
    main()
