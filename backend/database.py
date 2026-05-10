"""
Datenbankmodul für SQLite-Verbindung mit SQLAlchemy.
Stellt Engine, SessionLocal und Base bereit.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite-Datei wird im Projektroot erstellt
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Engine mit check_same_thread=False für SQLite in Multithreading-Umgebungen
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session-Factory für Datenbanktransaktionen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basisklasse für alle SQLAlchemy-Modelle
Base = declarative_base()


def get_db():
    """Dependency Injection für FastAPI — stellt DB-Session bereit."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
