from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from src.service.task_service import TaskService
from src.schema.task import TaskCreate, TaskUpdate
from src.schema.task import AssignTask
from src.routers.deps import require_roles
from src.routers.deps import get_current_user

router = APIRouter(prefix="/tasks")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

service = TaskService()

@router.post("/")
def create(data: TaskCreate, db: Session = Depends(get_db) , user = Depends(require_roles(["manager"]))):
    return service.create(db, data.title)

@router.patch("/{task_id}/assign")
def assign(
    task_id: str,
    data: AssignTask,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["manager"]))  
):
    return service.assign_task(db, task_id, data.user_id)

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/{task_id}")
def get_by_id(task_id: str, db: Session = Depends(get_db)):
    return service.get_by_id(db, task_id)

@router.patch("/{task_id}")
def update(
    task_id: str,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   # 🔥 REQUIRED
):
    return service.update(db, task_id, data, user)

@router.delete("/{task_id}")
def delete(task_id: str, db: Session = Depends(get_db)):
    return service.delete(db, task_id)