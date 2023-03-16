import enum

from sqlalchemy import Enum, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Note(BaseModel):
    __tablename__ = "note"

    class StatusEnum(enum.Enum):
        IN_PROGRESS = "in_progress"
        DONE = "done"

    text = Column(String(256))
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.IN_PROGRESS)
    list_id = Column(Integer, ForeignKey("list.id", ondelete="CASCADE"))

    list = relationship("ListTodo", back_populates="notes")
