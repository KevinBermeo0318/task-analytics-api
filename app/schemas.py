from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.models import TaskStatus

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, example="Estudiar")
    description: Optional[str] = Field(None, max_length=500, example="Estudiar para el examen de matemáticas")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, example="Estudiar")
    description: Optional[str] = Field(None, max_length=500, example="Estudiar para el examen de matemáticas")
    status: Optional[TaskStatus] = Field(None, example=TaskStatus.PENDING)

class ProductivityAnalytics(BaseModel):
    total_tasks: int = Field(..., example=10)
    completed_tasks: int = Field(..., example=5)
    pending_tasks: int = Field(..., example=3)
    in_progress_tasks: int = Field(..., example=2)
    completion_rate: float = Field(..., example=50.0)