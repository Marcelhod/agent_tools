from pathlib import Path
from .api import create_project_structure

def create_docker_compose(project_path: str) -> str:
    """Adds Docker Compose. Auto-creates the API if missing."""
    path = Path(project_path).resolve()
    
    if not path.exists():
        project_name = path.name
        target_dir = str(path.parent)
        create_project_structure(project_name, target_dir)

    project_name = path.name
    (path / "docker-compose.yml").write_text(
        "version: '3.8'\n"
        "services:\n"
        "  db:\n"
        "    image: postgres:15\n"
        "    environment:\n"
        f"      POSTGRES_DB: {project_name}\n"
        "  api:\n"
        "    build: .\n"
        "    ports:\n"
        "      - '8000:8000'\n"
    )
    return f"Docker Compose file created at {path}"