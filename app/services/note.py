from typing import TypeVar

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Note
from app.repositories.note import NoteRepository

PydanticModel = TypeVar('PydanticModel', bound=BaseModel)


class NoteServices:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
        self.repository = NoteRepository(self.session)

    async def create_note(self, input_schema: PydanticModel) -> Note:
        note = Note(**input_schema.dict())
        note = await self.repository.create(note)

        return note

    async def retrieve_note(self, note_id: int) -> Note:
        note = await self.repository.get_by_id(note_id)
        return note

    async def update_note(self, note_id: int, input_schema: PydanticModel) -> Result:
        values = input_schema.dict(exclude_unset=True)

        result = await self.repository.update(note_id, values)
        return result

    async def delete_note(self, note_id: int) -> Result:
        result = await self.repository.delete(note_id)
        return result

    async def mark_note_done(self, note_id: int) -> Result:
        values = {'status': Note.StatusEnum.DONE}

        result = await self.repository.update(note_id, values)
        return result

    async def mark_note_undone(self, note_id: int) -> Result:
        values = {'status': Note.StatusEnum.IN_PROGRESS}

        result = await self.repository.update(note_id, values)
        return result
