# Agent Tools (MCP Server)

An MCP (Model Context Protocol) server that enables AI agents to autonomously scaffold production-ready FastAPI applications, complete with databases, authentication, and Docker infrastructure.

## 🚀 What it does

This tool gives AI assistants (like Continue, Cursor, or Claude Desktop) the ability to build real backend applications directly on your local machine.

* `scaffold_database` — Adds a PostgreSQL database structure (SQLAlchemy). **Features "Auto-Heal":** If the API project doesn't exist yet, this tool will automatically generate the full FastAPI project structure first, then inject the database.
* `scaffold_auth` — Adds JWT authentication (passlib, python-jose) with login/register routes to an existing project.
* `scaffold_docker` — Generates a `docker-compose.yml` to orchestrate the API and Database.

## 💡 Why?

Setting up a new backend by hand is repetitive. This tool lets you tell your AI assistant: *"Create a full-stack app called test-app, add a database, add JWT auth, and add Docker"*—and have it actually do it, directly inside your editor.

## 📋 Requirements

* Python >= 3.10
* [uv](https://docs.astral.sh/uv/) (for packaging and running)
* An MCP-compatible client (e.g., Continue in VS Code)

## 🛠️ Usage

You don't need to clone this repository. You can run it directly via `uvx`.

### With Continue (VS Code)

Add this to your Continue `config.yaml`:

```yaml
mcpServers:
  - name: Agent tools
    command: uvx
    args:
      - "--from"
      - "git+https://github.com/Marcelhod/agent_tools.git"
      - "agent-tools"