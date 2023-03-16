from typing import TypeVar

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import ListTodo
from app.repositories.list import ListRepository

PydanticModel = TypeVar('PydanticModel', bound=BaseModel)


class ListServices:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
        self.repository = ListRepository(self.session)

    async def create_list(self, input_schema: PydanticModel) -> ListTodo:
        list_todo = ListTodo(**input_schema.dict())

        list_todo = await self.repository.create(list_todo)
        return list_todo

    async def retrieve_list(self, list_id: int) -> ListTodo:
        list_todo = await self.repository.get_by_id(list_id)
        await self._check_none_404(list_todo)

        return list_todo

    async def retrieve_list_with_notes(self, list_id: int) -> ListTodo:
        list_todo = await self.repository.get_by_id_with_notes(list_id)
        return list_todo

    async def retrieve_user_lists(self, user_id: int) -> list[ListTodo]:
        lists_todo = await self.repository.get_all_by_field("owner", user_id)
        return lists_todo

    async def update_list(self, list_id: int, input_schema: PydanticModel) -> Result:
        values = input_schema.dict(exclude_unset=True)

        result = await self.repository.update(list_id, values)
        return result

    async def delete_list(self, list_id: int) -> Result:
        result = await self.repository.delete(list_id)
        return result
