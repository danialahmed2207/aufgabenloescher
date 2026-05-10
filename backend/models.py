"""
SQLAlchemy-Modelle für die Datenbank.
Definiert die Tabellenstruktur der SQLite-Datenbank.
"""
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Task(Base):
    """Repräsentiert eine Aufgabe in der Datenbank."""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
