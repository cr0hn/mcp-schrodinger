# Changelog

## [0.1.1] - 2026-02-19

### Changed
- Complete README rewrite with professional open source structure
- Added badges, table of contents, detailed usage instructions for all MCP clients
- Added technical details section with architecture and payload explanation
- Added mitigations table and contributing guidelines
- Added step-by-step demo with expected outputs

## [0.1.0] - 2026-02-19

### Added
- Initial release of mcp-schrodinger PoC
- FastMCP server "Schrodinger Calculator" with `add` tool
- Safe behavior for first 3 calls (normal sum response)
- Prompt injection payload activated on 4th+ call
- Entry points: `mcp-schrodinger` CLI, `python -m mcp_schrodinger`
- pyproject.toml with hatchling build backend and uvx support
- README with security context, quick start, and usage instructions
- MIT License
