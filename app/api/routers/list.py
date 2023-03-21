from fastapi import APIRouter, Depends

from app.schemas.list import ListOut, ListCreate, ListUpdate, ListOutWithNotes
from app.services.list import ListServices

router = APIRouter()


@router.post("/lists", tags=['Lists'], response_model=ListOut)
async def create_list(input_schema: ListCreate, service: ListServices = Depends(ListServices)):
    list_todo = await service.create(input_schema)

    return list_todo


@router.get("/lists/{id}", tags=['Lists'], response_model=ListOut)
async def retrieve_list(list_id: int, service: ListServices = Depends(ListServices)):
    list_todo = await service.retrieve(list_id)

    return list_todo


@router.get("/lists/{id}/notes", tags=['Lists'], response_model=ListOutWithNotes)
async def retrieve_list_with_notes(list_id: int, service: ListServices = Depends(ListServices)):
    list_todo = await service.retrieve_with_notes(list_id)

    return list_todo


@router.get("/lists/user/{id}", tags=['Lists'], response_model=list[ListOut])
async def retrieve_user_lists(user_id: int, service: ListServices = Depends(ListServices)):
    lists_todo = await service.get_all_by_user_id(user_id=user_id)

    return lists_todo


@router.patch("/lists/{id}", tags=['Lists'], status_code=204)
async def update_list(list_id: int, input_schema: ListUpdate, service: ListServices = Depends(ListServices)):
    result = await service.update(list_id, input_schema)


@router.delete("/lists/{id}", tags=['Lists'], status_code=204)
async def delete_list(list_id: int, service: ListServices = Depends(ListServices)):
    result = await service.delete(list_id)
