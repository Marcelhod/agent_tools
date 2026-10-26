from mcp.server.mcpserver import MCPServer
from api_builder import create_project_structure, update_dependencies

mcp = MCPServer("APIBuilder")

@mcp.tool()
def scaffold_api(project_name: str, target_dir: str = ".") -> str:
    """Create a FastAPI project structure."""
    return create_project_structure(project_name, target_dir)

@mcp.tool()
def upgrade_deps(target_dir: str = ".") -> str:
    """Update dependencies for the uv project."""
    return update_dependencies(target_dir)

def main():
    mcp.run(transport="stdio")