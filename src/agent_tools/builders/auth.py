from pathlib import Path
import subprocess

def create_auth_structure(target_path: str) -> str:
    path = Path(target_path).resolve()
    if not path.exists():
        return f"Error: Directory '{path}' does not exist. Create the API first."

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

    subprocess.run(["uv", "add", "passlib[bcrypt]", "python-jose[cryptography]"], cwd=path, capture_output=True)
    return f"Auth structure added to {path}"