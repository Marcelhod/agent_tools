from mcp.server import MCPServer
from .builders import create_project_structure, update_dependencies, create_db_structure


mcp = MCPServer("Agenttools")

@mcp.tool()
def scaffold_api(project_name: str, target_dir: str = ".") -> str:
    """Create a FastAPI project structure."""
    return create_project_structure(project_name, target_dir)

@mcp.tool()
def upgrade_deps(target_dir: str = ".") -> str:
    """Update dependencies for the uv project."""
    return update_dependencies(target_dir)

@mcp.tool()
def scaffold_database(project_name: str, target_dir: str = ".") -> str:
    """Adds a PostgreSQL database structure (SQLAlchemy) to a project."""
    return create_db_structure(project_name, target_dir)


def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()