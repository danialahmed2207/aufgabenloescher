"""
Pydantic-Schemas für Request/Response-Validierung.
Sorgt für Typsicherheit in der REST API.
"""
from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    """Basis-Schema für gemeinsame Task-Felder."""
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    """Schema für das Erstellen einer neuen Aufgabe."""
    pass


class TaskUpdate(BaseModel):
    """Schema für partielle Updates — alle Felder optional."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskBase):
    """Vollständiges Schema für API-Responses inkl. ID."""
    id: int

    class Config:
        from_attributes = True
