from mcp.server import MCPServer
from .builders import (
    create_db_structure,
    create_auth_structure,
    create_docker_compose
)

mcp = MCPServer("Agenttools")

@mcp.tool()
def scaffold_database(project_path: str) -> str:
    """Adds a database to a project. Pass the folder path e.g., 'projects/test-app'."""
    return create_db_structure(project_path)

@mcp.tool()
def scaffold_auth(project_path: str) -> str:
    """Adds JWT auth to a project. Pass the folder path e.g., 'projects/test-app'."""
    return create_auth_structure(project_path)

@mcp.tool()
def scaffold_docker(project_path: str) -> str:
    """Adds Docker to a project. Pass the folder path e.g., 'projects/test-app'."""
    return create_docker_compose(project_path)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()