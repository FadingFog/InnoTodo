from fastapi import APIRouter, Depends

from app.api.routers import note
from app.api.routers import list as list_todo
from app.dependecies.auth import get_user_id_from_token

routes = APIRouter(dependencies=[Depends(get_user_id_from_token)])

routes.include_router(list_todo.router)
routes.include_router(note.router)
