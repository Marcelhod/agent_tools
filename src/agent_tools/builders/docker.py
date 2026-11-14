from pathlib import Path

def create_docker_compose(target_path: str) -> str:
    path = Path(target_path).resolve()
    if not path.exists():
        return f"Error: Directory '{path}' does not exist. Create the API first."

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