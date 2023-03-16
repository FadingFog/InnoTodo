from typing import TypeVar

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import User
from app.repositories.user import UserRepository
from app.utils import password_helper

PydanticModel = TypeVar('PydanticModel', bound=BaseModel)


class UserServices:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
        self.repository = UserRepository(self.session)

    async def create_user(self, input_schema: PydanticModel) -> User:
        hashed_password = password_helper.get_hash_password(input_schema.password)
        user = User(email=input_schema.email, hashed_password=hashed_password)

        user = await self.repository.create(user)
        return user

    async def retrieve_user(self, user_id: int) -> User:
        user = await self.repository.get_by_id_with_lists(user_id)
        return user

    async def retrieve_all_users(self) -> list[User]:
        users = await self.repository.get_all()
        return users

    async def update_user(self, user_id: int, input_schema: PydanticModel) -> Result:
        values = input_schema.dict(exclude_unset=True)

        result = await self.repository.update(user_id, values)
        return result

    async def delete_user(self, user_id: int) -> Result:
        result = await self.repository.delete(user_id)
        return result

    async def change_password(self, user_id: int, input_schema: PydanticModel) -> Result:
        new_password = password_helper.get_hash_password(input_schema.password)
        values = {'hashed_password': new_password}

        result = await self.repository.update(user_id, values)
        return result
