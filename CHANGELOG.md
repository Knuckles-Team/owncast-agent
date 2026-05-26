# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Action-Routed dynamic metaprogramming to drastically reduce tool limits while preserving 1:1 endpoint parity
- Pytest concept markers (`@pytest.mark.concept`) and docstring traceability mapping to the master concepts registry
- Full Environment Variables documentation section in README.md detailing 15 configuration settings

### Changed
- Replaced 122 independent tools with 4 tag-grouped dynamic routers
- Standardized tool schemas and removed any underscored parameters
- Refactored action routing in `mcp_server.py` to leverage dynamic method lookups based on strict sets of allowed actions, reducing module size by 64% and simplifying complexity
- Restructured `tests/` directory into cleanly isolated `tests/unit/` and `tests/integration/` suites
- Combined duplicate test client fixtures into a shared, reusable `tests/conftest.py`

### Fixed
- Pydantic V2 validations and Pytest failures related to missing parameters or schema conflicts
- Unused coroutine warning by correctly awaiting FastMCP's async `Context.info` calls
- Zero-assertion test cases by adding robust verification assertions to brute force API and reload scenarios

## [0.14.0] - 2026-04-29

### Added
- Initial release
