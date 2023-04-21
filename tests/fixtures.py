from typing import Optional

import pytest
from fastapi.requests import Request
from fastapi.testclient import TestClient
from jose import jwt

from app.api.routes import routes
from app.db import get_session
from app.dependecies.auth import get_user_id_from_token
from app.models import ListTodo
from app.repositories.list import ListRepository
from app.schemas.list import ListOut
from app.schemas.note import NoteOut
from app.utils import token_helper
from main import app
from tests.conftest import db_session_impl
from tests.factories import ListTodoFactory, NoteFactory


async def fake_user_id(request: Request):  # pragma: no cover
    request.state.user_id = 1


@pytest.fixture
def client():
    test_client = TestClient(app)

    app.user_middleware.clear()  # noqa
    app.middleware_stack = app.build_middleware_stack()

    app.dependency_overrides[get_user_id_from_token] = fake_user_id  # noqa
    app.dependency_overrides[get_session] = db_session_impl  # noqa

    return test_client


@pytest.fixture
def router():
    return routes


@pytest.fixture
def create_token():
    def _create(data: dict):
        encoded_jwt = jwt.encode(data, token_helper.PRIVATE_SECRET_KEY, algorithm=token_helper.ALGORITHM)
        return encoded_jwt
    return _create


@pytest.fixture
def create_list_todo():
    async def _create(values: Optional[dict] = None, add: bool = True) -> ListTodo:
        if values is None:
            values = {}

        if not add:
            list_todo = ListTodoFactory.build(**values)
        else:
            list_todo = await ListTodoFactory(**values)
        return list_todo

    return _create


@pytest.fixture
async def list_todo(create_list_todo) -> ListOut:
    list_orm = await create_list_todo()
    list_todo = ListOut.from_orm(list_orm)
    return list_todo


@pytest.fixture
async def note() -> NoteOut:
    note_orm = await NoteFactory()
    note = NoteOut.from_orm(note_orm)
    return note


@pytest.fixture
def list_repo(db_session) -> ListRepository:
    repo = ListRepository(db_session)
    return repo
