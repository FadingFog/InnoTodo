from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.list import ListOut


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    is_active: Optional[bool] = True


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class UserOutWithLists(UserOut):
    lists: list[ListOut] = []


class UserChangePassword(BaseModel):
    password: str
