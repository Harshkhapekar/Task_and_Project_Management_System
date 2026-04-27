from sqlalchemy.orm import declarative_base

Base = declarative_base()

from src.models.user import User
from src.models.project import Project
from src.models.task import Task