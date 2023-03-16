from fastapi import APIRouter, Depends, HTTPException

from app.schemas.list import ListOut, ListCreate, ListUpdate, ListByUser
from app.services.list import ListServices

router = APIRouter()


@router.post("/lists", tags=['Lists'], response_model=ListOut)
async def create_list(input_schema: ListCreate, service: ListServices = Depends(ListServices)):
    list_todo = await service.create_list(input_schema)

    return list_todo


@router.get("/lists/{id}", tags=['Lists'], response_model=ListOut)
async def retrieve_list(list_id: int, service: ListServices = Depends(ListServices)):
    list_todo = await service.retrieve_list(list_id)

    return list_todo


@router.get("/lists/{id}/notes", tags=['Lists'], response_model=ListOut)
async def retrieve_list_with_notes(list_id: int, service: ListServices = Depends(ListServices)):
    list_todo = await service.retrieve_list_with_notes(list_id)

    return list_todo


@router.get("/lists/", tags=['Lists'], response_model=list[ListOut])
async def retrieve_user_lists(input_schema: ListByUser, service: ListServices = Depends(ListServices)):
    lists_todo = await service.retrieve_user_lists(user_id=input_schema.user_id)

    return lists_todo


@router.patch("/lists/{id}", tags=['Lists'], status_code=204)
async def update_list(list_id: int, input_schema: ListUpdate, service: ListServices = Depends(ListServices)):
    result = await service.update_list(list_id, input_schema)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)


@router.delete("/lists/{id}", tags=['Lists'], status_code=204)
async def delete_list(list_id: int, service: ListServices = Depends(ListServices)):
    result = await service.delete_list(list_id)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)
