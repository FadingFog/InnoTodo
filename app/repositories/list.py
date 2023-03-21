from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.models import ListTodo
from app.repositories.base import BaseRepository, Model


class ListRepository(BaseRepository):
    model = ListTodo

    async def get_by_id_with_notes(self, list_id: int) -> Model:
        result = await self.session.scalars(
            select(self.model).where(self.model.id == list_id).options(joinedload(self.model.notes))
        )
        list_todo = result.unique().one_or_none()
        return list_todo
