from fastapi import Depends, HTTPException
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Note
from app.repositories.note import NoteRepository
from app.services.base import BaseServices


class NoteServices(BaseServices[Note]):
    repository = NoteRepository
    model = Note

    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(session)

    async def mark_note_done(self, note_id: int) -> Result:
        values = {'status': Note.StatusEnum.DONE}

        result = await self._repository.update(note_id, values)

        if result.rowcount < 1:
            raise HTTPException(status_code=404)

        return result

    async def mark_note_undone(self, note_id: int) -> Result:
        values = {'status': Note.StatusEnum.IN_PROGRESS}

        result = await self._repository.update(note_id, values)

        if result.rowcount < 1:
            raise HTTPException(status_code=404)

        return result
