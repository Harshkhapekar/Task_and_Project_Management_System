from sqlalchemy.orm import Session
from src.repository.user_repo import UserRepo
from src.models.user import User
from src.core.security import hash_password, verify_password, create_token

class AuthService:

    def __init__(self):
        self.repo = UserRepo()

    def login(self, db: Session, email: str, password: str):
        user = self.repo.get_by_email(db, email)

        if not user or not verify_password(password, user.password):
            raise Exception("Invalid credentials")

        return create_token({
            "sub": user.id,
            "email": user.email,
            "role": user.role
        })

    def register(self, db: Session, email: str, password: str, role: str):
        user = User(
            email=email,
            password=hash_password(password),
            role=role
        )
        return self.repo.create(db, user)