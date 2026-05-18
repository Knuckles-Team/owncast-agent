# Code Enhancement: owncast-agent

> Automated code enhancement review for owncast-agent. Covers 17 analysis domains.

## User Stories

- As a **developer**, I want to **address Project Analysis findings (grade: C, score: 74)**, so that **improve project project analysis from C to at least B (80+)**.
- As a **developer**, I want to **address Test Coverage findings (grade: D, score: 65)**, so that **improve project test coverage from D to at least B (80+)**.
- As a **developer**, I want to **address Architecture & Design Patterns findings (grade: C, score: 75)**, so that **improve project architecture & design patterns from C to at least B (80+)**.
- As a **developer**, I want to **address Concept Traceability findings (grade: F, score: 44)**, so that **improve project concept traceability from F to at least B (80+)**.
- As a **developer**, I want to **address Linting & Formatting findings (grade: F, score: 0)**, so that **improve project linting & formatting from F to at least B (80+)**.
- As a **developer**, I want to **address Changelog Audit findings (grade: C, score: 75)**, so that **improve project changelog audit from C to at least B (80+)**.
- As a **developer**, I want to **address Environment Variables findings (grade: C, score: 75)**, so that **improve project environment variables from C to at least B (80+)**.

## Functional Requirements

- **FR-001**: 1 functions exceed 200 lines (actionable refactoring targets): register_internal_tools (1435L)
- **FR-002**: Monolithic: mcp_server.py (1748L) — 1 functions with high complexity (worst: register_internal_tools at 1435L, CC=14); Low cohesion: 9 distinct concepts in one file
- **FR-003**: Needs attention: owncast_api.py (881L) — God class: OwncastApi (124 methods) — consider mixins/composition
- **FR-004**: Test suite lacks intent diversity (only one type)
- **FR-005**: 17 potential doc-test drift items
- **FR-006**: README.md missing sections: installation, usage|quick start
- **FR-007**: README missing: MCP tools mapping table with descriptions
- **FR-008**: README missing: Has a Table of Contents
- **FR-009**: README missing: Has usage examples with code blocks
- **FR-010**: README missing: References /docs directory material
- **FR-011**: README missing: Has MCP tools mapping table with descriptions
- **FR-012**: SRP: 2 modules exceed 500 lines (god modules)
- **FR-013**: SRP: 1 classes have >15 methods
- **FR-014**: No discernible layer architecture (no domain/service/adapter separation)
- **FR-015**: Low traceability ratio: 0% concepts fully traced
- **FR-016**: 3 test functions missing concept markers
- **FR-017**: 41 significant functions (>10 lines) missing concept markers in docstrings
- **FR-018**: Total lint findings: 122 (high/error: 122, medium/warning: 0, low: 0)
- **FR-019**: 2 hook(s) may be outdated: ruff-pre-commit, uv-pre-commit
- **FR-020**: CHANGELOG.md exists but could not be parsed — check format compliance
- **FR-021**: No changelog entries within the last 30 days
- **FR-022**: keepachangelog not installed — pip install 'universal-skills[code-enhancer]'
- **FR-023**: 1 tests have no assertions
- **FR-024**: Partial env var documentation: 34% coverage
- **FR-025**: Undocumented env vars: ALLOWED_CLIENT_REDIRECT_URIS, AUTH_TYPE, EUNOMIA_POLICY_FILE, EUNOMIA_REMOTE_URL, EUNOMIA_TYPE, OAUTH_BASE_URL, OAUTH_UPSTREAM_AUTH_ENDPOINT, OAUTH_UPSTREAM_CLIENT_ID, OAUTH_UPSTREAM_CLIENT_SECRET, OAUTH_UPSTREAM_TOKEN_ENDPOINT
- **FR-026**: 6 Python env vars not in .env.example: CHAT_TOOL, DEFAULT_AGENT_NAME, EXTERNAL_TOOL, INTERNAL_TOOL, OBJECTS_TOOL

## Success Criteria

- Overall GPA: 2.71 → 3.0
- Domains at B or above: 10 → 17
- Actionable findings: 26 → 0
