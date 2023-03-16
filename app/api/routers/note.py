from fastapi import APIRouter, Depends, HTTPException

from app.schemas.note import NoteCreate, NoteOut
from app.services.note import NoteServices

router = APIRouter()


@router.post("/notes", tags=['Notes'], response_model=NoteOut)
async def create_note(input_schema: NoteCreate, service: NoteServices = Depends(NoteServices)):
    note = await service.create_note(input_schema)

    return note


@router.get("/notes/{id}", tags=['Notes'], response_model=NoteOut)
async def retrieve_note(note_id: int, service: NoteServices = Depends(NoteServices)):
    note = await service.retrieve_note(note_id)

    return note


@router.patch("/notes/{id}", tags=['Notes'], status_code=204)
async def update_note(note_id: int, input_schema: NoteOut, service: NoteServices = Depends(NoteServices)):
    result = await service.update_note(note_id, input_schema)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)


@router.delete("/notes/{id}", tags=['Notes'], status_code=204)
async def delete_note(note_id: int, service: NoteServices = Depends(NoteServices)):
    result = await service.delete_note(note_id)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)


@router.post("/notes/{id}/done", tags=['Notes'])
async def mark_note_done(note_id: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_done(note_id)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)


@router.post("/notes/{id}/undone", tags=['Notes'])
async def mark_note_undone(note_id: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_undone(note_id)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)
