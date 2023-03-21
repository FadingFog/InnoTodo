from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class ListTodo(BaseModel):
    __tablename__ = "list"

    title = Column(String, index=True)
    owner_id = Column(Integer, nullable=False)

    notes = relationship("Note", back_populates="list")
