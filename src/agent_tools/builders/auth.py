from pathlib import Path
import subprocess
from .api import create_project_structure

def create_auth_structure(target_path: str) -> str:
    """Adds JWT authentication. Automatically creates the API if missing."""
    path = Path(target_path).resolve()
    
    # AUTO-HEAL
    if not path.exists():
        project_name = path.name
        target_dir = str(path.parent)
        create_project_structure(project_name, target_dir)

    auth_dir = path / "app" / "auth"
    auth_dir.mkdir(parents=True, exist_ok=True)
    (auth_dir / "__init__.py").write_text("")
    
    (auth_dir / "routes.py").write_text(
        "from fastapi import APIRouter\n\n"
        "router = APIRouter()\n\n"
        "@router.post('/login')\n"
        "def login():\n"
        "    return {'message': 'Login endpoint'}\n"
    )

    try:
        subprocess.run(["uv", "add", "passlib[bcrypt]", "python-jose[cryptography]"], cwd=path, capture_output=True, text=True, check=True)
        return f"Auth structure successfully added to {path}"
    except subprocess.CalledProcessError as e:
        return f"Auth files created, but dependency install failed: {e.stderr}"