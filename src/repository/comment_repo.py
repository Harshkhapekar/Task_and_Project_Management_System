from sqlalchemy.orm import Session
from src.models.comment import Comment

class CommentRepo:

    def create(self, db: Session, comment: Comment):
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    def get_by_id(self, db: Session, comment_id: str):
        return db.query(Comment).filter(Comment.id == comment_id).first()

    def update(self, db: Session, comment: Comment):
        db.commit()
        db.refresh(comment)
        return comment

    def delete(self, db: Session, comment: Comment):
        db.delete(comment)
        db.commit()