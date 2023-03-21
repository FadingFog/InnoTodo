from fastapi import APIRouter

from app.api.routers import note
from app.api.routers import list as list_todo

routes = APIRouter()

routes.include_router(list_todo.router)
routes.include_router(note.router)
