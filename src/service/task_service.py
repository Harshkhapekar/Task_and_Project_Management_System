from sqlalchemy.orm import Session
from src.repository.task_repo import TaskRepo
from src.models.task import Task

class TaskService:

    ALLOWED_TRANSITIONS = {
        "todo": ["in_progress"],
        "in_progress": ["review"],
        "review": ["qa"],
        "qa": ["done"],
        "done": []
    }

    def __init__(self):
        self.repo = TaskRepo()

    # ✅ CREATE
    def create(self, db: Session, title: str, project_id=None):
        return self.repo.create(db, Task(title=title, project_id=project_id))

    # ✅ ASSIGN TASK (manager only via router)
    def assign_task(self, db: Session, task_id: str, user_id: str):
        task = self.get_by_id(db, task_id)
        task.assigned_to = user_id
        return self.repo.update(db, task)

    # ✅ GET ALL
    def get_all(self, db: Session):
        return self.repo.get_all(db)

    # ✅ GET BY ID
    def get_by_id(self, db: Session, task_id: str):
        task = self.repo.get_by_id(db, task_id)
        if not task:
            raise Exception("Task not found")
        return task

    # ✅ UPDATE (WITH WORKFLOW + RBAC)
    def update(self, db: Session, task_id: str, data, user):
        task = self.get_by_id(db, task_id)

        # update title
        if data.title:
            task.title = data.title

        # update status with rules
        if data.status:

            # 🔥 workflow check
            if data.status not in self.ALLOWED_TRANSITIONS[task.status]:
                raise Exception("Invalid status transition")

            # 🔥 role rules
            if user["role"] == "developer" and data.status == "done":
                raise Exception("Developer cannot mark done")

            if user["role"] == "qa" and data.status != "done":
                raise Exception("QA can only move to done")

            task.status = data.status

        return self.repo.update(db, task)

    # ✅ DELETE
    def delete(self, db: Session, task_id: str):
        task = self.get_by_id(db, task_id)
        self.repo.delete(db, task)
        return {"msg": "deleted"}