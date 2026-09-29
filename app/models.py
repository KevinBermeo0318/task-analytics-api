import enum
from sqlalchemy import Colum, Integer, String ,Enum, DateTime, func
from app.database import Base

class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGESS = "in_Progress"
    COMPLETED = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id = Colum(Integer, primary_key=True, index=True)
    title = Colum(String, index=True, nullable=False)
    description = Colum(String, nullable=True)
    status = Colum(Enum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    created-att = Colum(DateTime(timezone=True), server_default=func.now())
    completed_at = Colum(DateTime(Timezone=True), nullable=True)
    