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
3. Keep changes inside this connector. Do not change `meristem`,
   `scion-sdk`, shared skills, runtime deployment, or service configuration.
4. Work in a private real Git worktree on a distinct branch. Never use harness worktree
   isolation, `git stash`, `git add -A`, or `git add .` in this shared repository.
5. Run focused checks for the changed behavior and the repository's normal pre-commit
   hooks. Keep the lockfile current when changing dependencies.
6. Review the complete diff, stage only reviewed paths, and open one pull request for the
   coherent change. Let normal CI and release workflows publish the package and docs.

## Steps

1. Read `AGENTS.md` and run `git status --short` and verify the working tree holds only the files you intend to change.
2. Find the owning spec row with `git grep -n "<term>" -- specs` and verify the row id you will cite in the `Spec:` trailer.
3. Make the change inside this connector only and verify `git diff --stat` lists no path outside it.
4. Run `uv run pytest tests -q --tb=short -m "not slow" --timeout=60` and verify the run ends with zero failures.
5. Run `pre-commit run --all-files` and verify every hook reports Passed.
6. Commit with the `Spec:` trailer adjacent to the agent trailer and verify `git log -1` shows both in the final paragraph.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| 401 or 403 response | `OWNCAST_TOKEN` is missing or lacks admin scope, or `OWNCAST_URL` points at the wrong instance | Set `OWNCAST_URL` and an admin `OWNCAST_TOKEN` in the environment, restart the server, and repeat the first read call |
| Tests fail on import | The environment is not synced with the lock file | Run `uv sync --locked --all-extras` and rerun the focused test command |
| Pre-commit hook fails | The change broke a shared connector gate | Read the hook output, fix the reported file, and rerun `pre-commit run --all-files` without bypassing the hook |
| No owning spec row found | The behaviour is not yet specified | Add the row to the owning spec under `specs/` before changing code, then cite its id |

## Local checks

- Focused tests: `uv run pytest tests -q --tb=short -m "not slow" --timeout=60`
- Commit hooks: `pre-commit run --all-files`
- Before a release, use the configured version bumper and regenerate `uv.lock` only when
  dependency metadata changes.
