---
name: owncast-agent-development
skill_type: skill
description: Develop and deliver changes in the Owncast connector repository.
---

# Owncast Agent Development

Use this skill for work in the `owncast-agent` repository. The repository owns the
Owncast API client, mappings, connector content, MCP tools, and the companion agent.
The connector contract and generic MCP/A2A transports belong to
[`scion-sdk`](https://github.com/Knuckles-Team/scion-sdk).

## Rapid delivery: the 5-minute contract

1. Read this repository's `AGENTS.md` and inspect `git status --short` before editing.
2. Find the owning row with `git grep -n "<term>" -- specs` and follow the spec standard.
   Add the row to the owning spec before changing behavior. Cite its ID in a `Spec:` trailer.
3. Keep changes inside this connector. Do not change `agent-utilities`,
   `scion-sdk`, shared skills, runtime deployment, or service configuration.
4. Work in a private real Git worktree on a distinct branch. Never use harness worktree
   isolation, `git stash`, `git add -A`, or `git add .` in this shared repository.
5. Run focused checks for the changed behavior and the repository's normal pre-commit
   hooks. Keep the lockfile current when changing dependencies.
6. Review the complete diff, stage only reviewed paths, and open one pull request for the
   coherent change. Let normal CI and release workflows publish the package and docs.

## Local checks

- Focused tests: `uv run pytest tests -q --tb=short -m "not slow" --timeout=60`
- Commit hooks: `pre-commit run --all-files`
- Before a release, use the configured version bumper and regenerate `uv.lock` only when
  dependency metadata changes.
