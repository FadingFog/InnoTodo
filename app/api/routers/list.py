from fastapi import APIRouter, Depends, Request

from app.schemas.list import ListOut, ListCreate, ListUpdate, ListOutWithNotes, ListCreateInternal
from app.services.list import ListServices

router = APIRouter(tags=['Lists'])


@router.post("/lists", response_model=ListOut)
async def create_list(request: Request, input_schema: ListCreate, service: ListServices = Depends(ListServices)):
    create_schema = ListCreateInternal(owner_id=request.state.user_id, **input_schema.dict())
    list_todo = await service.create(create_schema)

    return list_todo


@router.get("/lists/{pk}", response_model=ListOut)
async def retrieve_list(pk: int, service: ListServices = Depends(ListServices)):
    list_todo = await service.retrieve(pk)

    return list_todo


@router.get("/lists/{pk}/notes", response_model=ListOutWithNotes)
async def retrieve_list_with_notes(pk: int, service: ListServices = Depends(ListServices)):
    list_todo = await service.retrieve_with_notes(pk)

    return list_todo


@router.get("/lists/user/{pk}", response_model=list[ListOut])
async def retrieve_user_lists(pk: int, service: ListServices = Depends(ListServices)):
    lists_todo = await service.get_all_by_user_id(user_id=pk)

    return lists_todo


@router.patch("/lists/{pk}", status_code=204)
async def update_list(pk: int, input_schema: ListUpdate, service: ListServices = Depends(ListServices)):
    result = await service.update(pk, input_schema)


@router.delete("/lists/{pk}", status_code=204)
async def delete_list(pk: int, service: ListServices = Depends(ListServices)):
    result = await service.delete(pk)
