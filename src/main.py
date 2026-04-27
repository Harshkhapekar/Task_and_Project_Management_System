from fastapi import FastAPI
from src.db.base import Base
from src.db.session import engine
from src.routers.task import router as task_router
from src.routers.auth import router as auth_router
from src.routers.comment import router as comment_router
from fastapi.security import HTTPBearer

app = FastAPI()
security = HTTPBearer()
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(comment_router)