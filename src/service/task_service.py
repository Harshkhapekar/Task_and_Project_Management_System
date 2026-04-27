from sqlalchemy.orm import Session
from src.repository.task_repo import TaskRepo
from src.models.task import Task

class TaskService:

    def __init__(self):
        self.repo = TaskRepo()

    def create(self, db: Session, title: str):
        return self.repo.create(db, Task(title=title))

    def get_all(self, db: Session):
        return self.repo.get_all(db)

    def get_by_id(self, db: Session, task_id: str):
        task = self.repo.get_by_id(db, task_id)
        if not task:
            raise Exception("Not found")
        return task

    def update(self, db: Session, task_id: str, data):
        task = self.get_by_id(db, task_id)

        if data.title:
            task.title = data.title
        if data.status:
            task.status = data.status

        return self.repo.update(db, task)

    def delete(self, db: Session, task_id: str):
        task = self.get_by_id(db, task_id)
        self.repo.delete(db, task)
        return {"msg": "deleted"}