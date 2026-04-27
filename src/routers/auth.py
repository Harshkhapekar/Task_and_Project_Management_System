from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from src.db.session import SessionLocal
from src.service.auth_service import AuthService
from src.schema.user import UserCreate
from src.routers.deps import require_roles   # 🔥 ADD

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

service = AuthService()


# 🔐 LOGIN
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        token = service.login(db, form_data.username, form_data.password)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 👤 CREATE USER (ADMIN ONLY)
@router.post("/create-user")
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["manager"]))  
):
    try:
        return service.register(db, data.email, data.password, data.role)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))