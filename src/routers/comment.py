from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.session import SessionLocal
from src.service.comment_service import CommentService
from src.schema.comment import CommentCreate, CommentUpdate
from src.routers.deps import get_current_user

router = APIRouter(prefix="/comments", tags=["comments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

service = CommentService()


# ✅ POST
@router.post("/")
def create(
    data: CommentCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return service.create(db, data.content, data.task_id, user["sub"])


# ✅ GET
@router.get("/{comment_id}")
def get(comment_id: str, db: Session = Depends(get_db)):
    return service.get_by_id(db, comment_id)


# ✅ PATCH
@router.patch("/{comment_id}")
def update(
    comment_id: str,
    data: CommentUpdate,
    db: Session = Depends(get_db)
):
    return service.update(db, comment_id, data.content)


# ✅ DELETE
@router.delete("/{comment_id}")
def delete(comment_id: str, db: Session = Depends(get_db)):
    return service.delete(db, comment_id)