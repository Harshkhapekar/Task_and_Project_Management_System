# src/service/project_service.py
from sqlalchemy.orm import Session
from src.repository.project_repo import ProjectRepo
from src.models.project import Project

class ProjectService:

    def __init__(self):
        self.repo = ProjectRepo()

    def create(self, db: Session, name: str):
        return self.repo.create(db, Project(name=name))

    def get_all(self, db: Session):
        return self.repo.get_all(db)

    def get_by_id(self, db: Session, project_id: str):
        project = self.repo.get_by_id(db, project_id)
        if not project:
            raise Exception("Project not found")
        return project

    def delete(self, db: Session, project_id: str):
        project = self.get_by_id(db, project_id)
        self.repo.delete(db, project)
        return {"msg": "deleted"}