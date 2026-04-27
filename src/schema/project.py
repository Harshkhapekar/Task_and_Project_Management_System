# src/schema/project.py
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str