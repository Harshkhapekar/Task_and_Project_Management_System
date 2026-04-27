# src/routers/project.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from src.service.project_service import ProjectService
from src.schema.project import ProjectCreate

router = APIRouter(prefix="/projects", tags=["projects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

service = ProjectService()

@router.post("/")
def create(data: ProjectCreate, db: Session = Depends(get_db)):
    return service.create(db, data.name)

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/{project_id}")
def get_by_id(project_id: str, db: Session = Depends(get_db)):
    return service.get_by_id(db, project_id)

@router.delete("/{project_id}")
def delete(project_id: str, db: Session = Depends(get_db)):
    return service.delete(db, project_id)