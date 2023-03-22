from fastapi import APIRouter, Depends

from app.schemas.note import NoteCreate, NoteOut
from app.services.note import NoteServices

router = APIRouter(tags=['Notes'])


@router.post("/notes", response_model=NoteOut)
async def create_note(input_schema: NoteCreate, service: NoteServices = Depends(NoteServices)):
    note = await service.create(input_schema)

    return note


@router.get("/notes/{pk}", response_model=NoteOut)
async def retrieve_note(pk: int, service: NoteServices = Depends(NoteServices)):
    note = await service.retrieve(pk)

    return note


@router.patch("/notes/{pk}", status_code=204)
async def update_note(pk: int, input_schema: NoteOut, service: NoteServices = Depends(NoteServices)):
    result = await service.update(pk, input_schema)


@router.delete("/notes/{pk}", status_code=204)
async def delete_note(pk: int, service: NoteServices = Depends(NoteServices)):
    result = await service.delete(pk)


@router.post("/notes/{pk}/done")
async def mark_note_done(pk: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_done(pk)


@router.post("/notes/{pk}/undone")
async def mark_note_undone(pk: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_undone(pk)
