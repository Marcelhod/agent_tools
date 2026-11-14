from mcp.server import MCPServer
from .builders import (
    create_project_structure, 
    update_dependencies, 
    create_db_structure,
    create_auth_structure,
    create_docker_compose
)

mcp = MCPServer("Agenttools")

@mcp.tool()
def scaffold_api(project_name: str, target_dir: str = ".") -> str:
    """Create a FastAPI project structure. (Only this tool uses project_name and target_dir)."""
    return create_project_structure(project_name, target_dir)

@mcp.tool()
def upgrade_deps(target_dir: str = ".") -> str:
    """Update dependencies for the uv project."""
    return update_dependencies(target_dir)

@mcp.tool()
def scaffold_database(target_path: str) -> str:
    """Adds a database structure. Pass the exact path (e.g., 'projects/my-app')."""
    return create_db_structure(target_path)

@mcp.tool()
def scaffold_auth(target_path: str) -> str:
    """Adds JWT authentication. Pass the exact path (e.g., 'projects/my-app')."""
    return create_auth_structure(target_path)

@mcp.tool()
def scaffold_docker(target_path: str) -> str:
    """Adds Docker Compose. Pass the exact path (e.g., 'projects/my-app')."""
    return create_docker_compose(target_path)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()