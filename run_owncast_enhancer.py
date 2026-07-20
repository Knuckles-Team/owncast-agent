import importlib.util
import json
import os
import sys
import time
from pathlib import Path

from agent_utilities.security.persistence_privacy import sanitize_for_persistence

scripts_dir_value = os.getenv("CODE_ENHANCER_SCRIPTS_DIR")
if not scripts_dir_value:
    print("CODE_ENHANCER_SCRIPTS_DIR must be configured", file=sys.stderr)
    raise SystemExit(2)
scripts_dir = Path(scripts_dir_value).expanduser().resolve()
project_dir = str(Path(__file__).parent.resolve())

analyzers = [
    ("analyze_project", "analyze_project"),
    ("audit_dependencies", "audit_dependencies"),
    ("analyze_codebase", "analyze_codebase"),
    ("analyze_security", "analyze_security"),
    ("analyze_tests", "analyze_tests"),
    ("audit_documentation", "audit_documentation"),
    ("analyze_architecture", "analyze_architecture"),
    ("trace_concepts", "trace_concepts"),
    ("run_linters", "run_linters"),
    ("run_precommit", "run_precommit"),
    ("run_tests", "run_tests"),
    ("analyze_directory_density", "analyze_directory_density"),
    ("analyze_ui", "analyze_ui"),
    ("analyze_version_sync", "analyze_version_sync"),
    ("audit_changelog", "audit_changelog"),
    ("grade_pytest", "grade_pytest"),
    ("scan_env_vars", "scan_env_vars"),
]

results = []

for module_name, func_name in analyzers:
    print(f"Running {module_name}...", flush=True)
    try:
        spec = importlib.util.spec_from_file_location(
            module_name, str(scripts_dir / f"{module_name}.py")
        )
        if spec is None or spec.loader is None:
            print(f"  -> Spec/loader not found for {module_name}", flush=True)
            continue
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        func = getattr(mod, func_name)

        start = time.monotonic()
        result = func(project_dir)
        elapsed = time.monotonic() - start
        print(
            f"  -> Success in {elapsed:.2f}s, score: {result.get('score')}", flush=True
        )
        results.append(result)
    except Exception as exc:
        print(
            f"  -> ERROR running {module_name}: {type(exc).__name__}", flush=True
        )

print("\nGenerating report...", flush=True)
if str(scripts_dir) not in sys.path:
    sys.path.append(str(scripts_dir))
import generate_report

report_path = str(Path(__file__).parent / ".specify" / "reports" / "report.md")
Path(report_path).parent.mkdir(parents=True, exist_ok=True)
safe_results, _privacy_report = sanitize_for_persistence(results)
generate_report.generate_report(
    safe_results, project_name="owncast-agent", output_path=report_path
)
print("Report saved successfully", flush=True)

# Save results.json
results_json_path = str(Path(__file__).parent / ".specify" / "results.json")
with open(results_json_path, "w") as f:
    json.dump(safe_results, f, indent=2)
print("Results JSON saved successfully", flush=True)

print("Generating SDD handoff...", flush=True)
import generate_sdd_handoff

handoff = generate_sdd_handoff.generate_sdd_handoff(
    safe_results, project_name="owncast-agent", output_dir=project_dir
)
print("SDD handoff generated successfully!", flush=True)
print("All done!", flush=True)
