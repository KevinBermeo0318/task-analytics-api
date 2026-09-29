from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Task, TaskStatus
from app.schemas import ProductivityAnalytics

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/", response_model=ProductivityAnalytics)
def get_productivity_analytics(db: Session = Depends(get_db)):
    """Retrieve productivity analytics based on tasks in the database."""
    total_tasks = db.query(Task).count()
    completed_tasks = db.query(Task).filter(Task.status == TaskStatus.COMPLETED).count()
    pending_tasks = db.query(Task).filter(Task.status == TaskStatus.PENDING).count()
    in_progress_tasks = db.query(Task).filter(Task.status == TaskStatus.IN_PROGESS).count()

    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0.0

    return ProductivityAnalytics(
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        in_progress_tasks=in_progress_tasks,
        completion_rate=completion_rate
    )

