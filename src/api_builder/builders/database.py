import pathlib

def create_db_structure(project_name: str, target_dir: str = ".") -> str:
    base_path = pathlib.Path(target_dir).expanduser().resolve() / project_name
    base_path.mkdir(parents=True, exist_ok=True)

    # Create DB folder
    (base_path / "db").mkdir(exist_ok=True)
    
    # Write a basic SQLAlchemy setup
    (base_path / "db" / "session.py").write_text(
        "from sqlalchemy import create_engine\n"
        "from sqlalchemy.orm import sessionmaker\n\n"
        "SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@localhost/dbname'\n"
        "engine = create_engine(SQLALCHEMY_DATABASE_URL)\n"
        "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n"
    )

    return f"Successfully added database structure to {base_path}"