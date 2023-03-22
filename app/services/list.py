from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import ListTodo
from app.repositories.list import ListRepository
from app.services.base import BaseServices


class ListServices(BaseServices[ListTodo]):
    repository = ListRepository
    model = ListTodo

    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(session)

    async def retrieve_with_notes(self, list_id: int) -> ListTodo:
        list_todo = await self._repository.get_by_id_with_notes(list_id)
        await self._check_obj_404(list_todo)

        return list_todo

    async def get_all_by_user_id(self, user_id: int) -> list[ListTodo]:
        lists_todo = await self._repository.get_all_by_field("owner_id", user_id)

        return lists_todo
