from typing import Optional

from pydantic import BaseModel

from app.schemas.note import NoteOut


class ListCreate(BaseModel):
    owner_id: int
    title: str


class ListUpdate(BaseModel):
    title: Optional[str]


class ListOut(BaseModel):
    id: int
    owner_id: int
    title: str

    class Config:
        orm_mode = True


class ListOutWithNotes(ListOut):
    notes: list[NoteOut] = []


class ListByUser(BaseModel):
    user_id: int