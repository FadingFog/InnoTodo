import pytest
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.security import HTTPAuthorizationCredentials

from app.dependecies.auth import get_user_id_from_token


async def test_get_user_id_from_token_return_user_id(create_token):
    data = {"user_id": 1}
    encoded_jwt = create_token(data)
    access_token = HTTPAuthorizationCredentials(scheme="test", credentials=encoded_jwt)
    request = Request(scope={"type": "http"})

    user_id = await get_user_id_from_token(request, access_token=access_token)

    assert user_id == data["user_id"]


async def test_get_user_id_from_token_raise_http_exception_if_user_id_not_in_token(create_token):
    data = {"test": "yes"}
    encoded_jwt = create_token(data)
    access_token = HTTPAuthorizationCredentials(scheme="test", credentials=encoded_jwt)
    request = Request(scope={"type": "http"})

    with pytest.raises(HTTPException):
        user_id = await get_user_id_from_token(request, access_token=access_token)


async def test_get_user_id_from_token_raise_http_exception_if_token_not_valid(create_token):
    encoded_jwt = "test_not_valid_jwt"
    access_token = HTTPAuthorizationCredentials(scheme="test", credentials=encoded_jwt)
    request = Request(scope={"type": "http"})

    with pytest.raises(HTTPException):
        user_id = await get_user_id_from_token(request, access_token=access_token)
