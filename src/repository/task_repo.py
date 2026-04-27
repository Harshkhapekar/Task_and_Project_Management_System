from sqlalchemy.orm import Session
from src.models.task import Task

class TaskRepo:

    def create(self, db: Session, task: Task):
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def get_all(self, db: Session):
        return db.query(Task).all()

    def get_by_id(self, db: Session, task_id: str):
        return db.query(Task).filter(Task.id == task_id).first()

    def update(self, db: Session, task: Task):
        db.commit()
        db.refresh(task)
        return task

    def delete(self, db: Session, task: Task):
        db.delete(task)
        db.commit()