from typing import Optional

from pydantic import BaseModel

from app.models.note import Note


class NoteCreate(BaseModel):
    list_id: int
    text: str
    status: Note.StatusEnum = Note.StatusEnum.IN_PROGRESS


class NoteUpdate(BaseModel):
    text: Optional[str] = True
    status: Optional[Note.StatusEnum]


class NoteOut(BaseModel):
    id: int
    list_id: int
    text: str
    status: Note.StatusEnum

    class Config:
        orm_mode = True
