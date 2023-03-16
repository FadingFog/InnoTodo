from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class ListTodo(BaseModel):
    __tablename__ = "list"

    title = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))

    owner = relationship("User", back_populates="lists")
    notes = relationship("Note", back_populates="list")
