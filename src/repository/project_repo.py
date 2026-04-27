# src/repository/project_repo.py
from sqlalchemy.orm import Session
from src.models.project import Project

class ProjectRepo:

    def create(self, db: Session, project: Project):
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    def get_all(self, db: Session):
        return db.query(Project).all()

    def get_by_id(self, db: Session, project_id: str):
        return db.query(Project).filter(Project.id == project_id).first()

    def delete(self, db: Session, project: Project):
        db.delete(project)
        db.commit()