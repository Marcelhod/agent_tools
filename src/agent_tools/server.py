from mcp.server import MCPServer
from .builders import (
    create_db_structure,
    create_auth_structure,
    create_docker_compose
)

mcp = MCPServer("Agenttools")

@mcp.tool()
def scaffold_database(target_path: str) -> str:
    """Adds a database to an existing project. If the project doesn't exist, it automatically creates it."""
    return create_db_structure(target_path)

@mcp.tool()
def scaffold_auth(target_path: str) -> str:
    """Adds JWT auth to an existing project."""
    return create_auth_structure(target_path)

@mcp.tool()
def scaffold_docker(target_path: str) -> str:
    """Adds Docker Compose to an existing project."""
    return create_docker_compose(target_path)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()