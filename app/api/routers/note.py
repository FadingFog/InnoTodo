from fastapi import APIRouter, Depends, Request
from fastapi_signals import initiate_task

from app.schemas.note import NoteCreate, NoteOut, NoteUpdate
from app.services.note import NoteServices
from app.tasks import statistics_handler, ActionEnum

router = APIRouter(tags=['Notes'])


@router.post("/notes", response_model=NoteOut)
async def create_note(request: Request, input_schema: NoteCreate, service: NoteServices = Depends(NoteServices)):
    note = await service.create(input_schema)
    await initiate_task(statistics_handler, user_id=request.state.user_id, action=ActionEnum.NOTE_CREATE)

    return note


@router.get("/notes/{pk}", response_model=NoteOut)
async def retrieve_note(pk: int, service: NoteServices = Depends(NoteServices)):
    note = await service.retrieve(pk)

    return note


@router.patch("/notes/{pk}", status_code=204)
async def update_note(pk: int, input_schema: NoteUpdate, service: NoteServices = Depends(NoteServices)):
    result = await service.update(pk, input_schema)


@router.delete("/notes/{pk}", status_code=204)
async def delete_note(request: Request, pk: int, service: NoteServices = Depends(NoteServices)):
    result = await service.delete(pk)
    await initiate_task(statistics_handler, user_id=request.state.user_id, action=ActionEnum.NOTE_DELETE)


@router.post("/notes/{pk}/done")
async def mark_note_done(request: Request, pk: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_done(pk)
    await initiate_task(statistics_handler, user_id=request.state.user_id, action=ActionEnum.NOTE_MARKED_DONE)


@router.post("/notes/{pk}/undone")
async def mark_note_undone(request: Request, pk: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_undone(pk)
    await initiate_task(statistics_handler, user_id=request.state.user_id, action=ActionEnum.NOTE_MARKED_UNDONE)
