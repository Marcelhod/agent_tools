from pathlib import Path
from .api import create_project_structure

def create_db_structure(target_path: str) -> str:
    """Adds a database structure. Automatically creates the API if missing."""
    path = Path(target_path).resolve()
    
    # AUTO-HEAL: If the folder doesn't exist, build the API first!
    if not path.exists():
        project_name = path.name
        target_dir = str(path.parent)
        create_project_structure(project_name, target_dir)

    db_dir = path / "app" / "db"
    db_dir.mkdir(parents=True, exist_ok=True)
    (db_dir / "__init__.py").write_text("")
    
    (db_dir / "session.py").write_text(
        "from sqlalchemy import create_engine\n"
        "from sqlalchemy.orm import sessionmaker\n"
        "SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@localhost/dbname'\n"
        "engine = create_engine(SQLALCHEMY_DATABASE_URL)\n"
        "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n"
    )
    return f"Database structure successfully added to {path}"