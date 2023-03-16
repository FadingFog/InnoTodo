from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    lists = relationship("ListTodo", back_populates="owner")
