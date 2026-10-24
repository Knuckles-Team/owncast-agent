"""Basic startup smoke tests."""

import subprocess
import sys



def test_module_runnable():
    """Package module should be runnable with --help or similar."""
    pkg_name = (
        __import__("tomllib").loads(__import__("pathlib").Path(__file__).resolve().parent.parent.joinpath("pyproject.toml").read_text(encoding="utf-8"))["project"]["name"].replace("-", "_")
    )
    result = subprocess.run(
        [sys.executable, "-c", f"import {pkg_name}"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, f"Import failed: {result.stderr}"
