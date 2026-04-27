import uuid
from sqlalchemy import Column, String, ForeignKey
from src.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    status = Column(String, default="todo")
    assigned_to = Column(String, ForeignKey("users.id"), nullable=True)