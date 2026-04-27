from sqlalchemy.orm import Session
from src.repository.comment_repo import CommentRepo
from src.models.comment import Comment

class CommentService:

    def __init__(self):
        self.repo = CommentRepo()

    def create(self, db: Session, content: str, task_id: str, user_id: str):
        return self.repo.create(
            db,
            Comment(content=content, task_id=task_id, user_id=user_id)
        )

    def get_by_id(self, db: Session, comment_id: str):
        comment = self.repo.get_by_id(db, comment_id)
        if not comment:
            raise Exception("Not found")
        return comment

    def update(self, db: Session, comment_id: str, content: str):
        comment = self.get_by_id(db, comment_id)
        comment.content = content
        return self.repo.update(db, comment)

    def delete(self, db: Session, comment_id: str):
        comment = self.get_by_id(db, comment_id)
        self.repo.delete(db, comment)
        return {"msg": "deleted"}