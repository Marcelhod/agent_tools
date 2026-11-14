from pathlib import Path

def create_db_structure(target_path: str) -> str:
    path = Path(target_path).resolve()
    if not path.exists():
        return f"Error: Directory '{path}' does not exist. Create the API first."

    db_dir = path / "app" / "db"
    db_dir.mkdir(parents=True, exist_ok=True)
    
    (db_dir / "session.py").write_text(
        "from sqlalchemy import create_engine\n"
        "from sqlalchemy.orm import sessionmaker\n"
        "SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@localhost/dbname'\n"
        "engine = create_engine(SQLALCHEMY_DATABASE_URL)\n"
        "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n"
    )
    return f"Database structure added to {path}"