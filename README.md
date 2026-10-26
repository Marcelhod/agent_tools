# api-builder

An MCP (Model Context Protocol) server that lets AI agents scaffold complete FastAPI projects and manage their dependencies.

## What it does

- `scaffold_api` — Creates a ready-to-run FastAPI project (app package, routers, Dockerfile, .gitignore, dependencies installed).
- `upgrade_deps` — Upgrades a uv project's locked dependencies and syncs the environment.

## Why

Setting up a new FastAPI project by hand is repetitive. This tool lets you tell your AI assistant "create a FastAPI project called X" and have it actually do it, inside your editor.

## Requirements

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/)
- An MCP-compatible client (e.g. Continue in VS Code)

## Usage

### With Continue (MCP)

Add to your Continue MCP config:

```yaml
mcpServers:
  - name: API Builder
    type: stdio
    command: uv
    args:
      - run
      - --directory
      - /path/to/api-builder
      - api-builder
```

Then in Agent mode, ask: "Create a FastAPI project called demo in ~/projects."

### Standalone

If you want to call the underlying function directly without an MCP client:

```bash
uv run python -c "from api_builder import create_project_structure; print(create_project_structure('demo'))"
```

## Tech

Python, MCP SDK, uv, FastAPI.