from fastapi import Depends, HTTPException
from fastapi import status
from fastapi.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError

from app.utils import token_helper

auth_scheme = HTTPBearer()


async def get_user_id_from_token(request: Request, access_token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = access_token.credentials

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"Authentication": "Bearer"},
    )

    try:
        payload = token_helper.get_token_payload(token)
        user_id: int = payload.get("user_id")
        if not user_id:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    request.state.user_id = user_id

    return user_id
