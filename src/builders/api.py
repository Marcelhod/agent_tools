import subprocess
from pathlib import Path


def create_project_structure(project_name: str, target_dir: str = ".") -> str:
    """Create a complete FastAPI project in the specified directory."""
    target_path = Path(target_dir) / project_name
    if target_path.exists():
        return f"Error: directory '{target_path}' already exists."

    try:
        # 1. Base uv project
        subprocess.run(
            ["uv", "init", str(target_path)],
            capture_output=True, text=True, check=True
        )

        # 2. FastAPI app package
        app_dir = target_path / "app"
        app_dir.mkdir()
        (app_dir / "__init__.py").write_text("")
        (app_dir / "main.py").write_text(
            "from fastapi import FastAPI\n"
            "\n"
            "app = FastAPI(title=\"" + project_name + "\")\n"
            "\n"
            "@app.get(\"/\")\n"
            "def read_root():\n"
            "    return {\"message\": \"Hello from " + project_name + "\"}\n"
        )

        # 3. Routers package (empty, ready for endpoints)
        routers_dir = app_dir / "routers"
        routers_dir.mkdir()
        (routers_dir / "__init__.py").write_text("")

        # 4. Install runtime dependencies
        subprocess.run(
            ["uv", "add", "fastapi", "uvicorn[standard]"],
            cwd=target_path, capture_output=True, text=True, check=True
        )

        # 5. Dockerfile
        (target_path / "Dockerfile").write_text(
            "FROM python:3.12-slim\n"
            "WORKDIR /app\n"
            "COPY pyproject.toml uv.lock ./\n"
            "RUN pip install uv && uv sync --frozen\n"
            "COPY . .\n"
            "CMD [\"uv\", \"run\", \"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n"
        )

        # 6. .gitignore
        (target_path / ".gitignore").write_text(
            "__pycache__/\n"
            "*.pyc\n"
            ".venv/\n"
            ".env\n"
        )

        return (
            f"FastAPI project '{project_name}' created at {target_path}.\n"
            f"Run it with: cd {target_path} && uv run uvicorn app.main:app --reload"
        )

    except subprocess.CalledProcessError as e:
        return f"Failed to create project: {e.stderr}"
    except Exception as e:
        return f"Unexpected error: {e}"


def update_dependencies(target_dir: str = ".") -> str:
    """Update dependencies for the uv project in the target directory."""
    try:
        lock = subprocess.run(
            ["uv", "lock", "--upgrade"],
            cwd=target_dir, capture_output=True, text=True, check=True
        )
        sync = subprocess.run(
            ["uv", "sync"],
            cwd=target_dir, capture_output=True, text=True, check=True
        )
        return f"Dependencies updated.\nLock: {lock.stdout}\nSync: {sync.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Update failed: {e.stderr}"