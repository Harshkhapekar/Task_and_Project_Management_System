from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    project_id: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None

class TaskResponse(BaseModel):
    id: str
    title: str
    status: str

class AssignTask(BaseModel):
    user_id: str

    class Config:
        from_attributes = True