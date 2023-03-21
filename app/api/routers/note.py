from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.schemas.note import NoteCreate, NoteOut
from app.services.note import NoteServices

router = APIRouter()


@router.get("/aboba")
async def get_aboba(request: Request):
    header = request.headers.get('Authorization')
    return JSONResponse({'header': header})


@router.post("/notes", tags=['Notes'], response_model=NoteOut)
async def create_note(input_schema: NoteCreate, service: NoteServices = Depends(NoteServices)):
    note = await service.create(input_schema)

    return note


@router.get("/notes/{id}", tags=['Notes'], response_model=NoteOut)
async def retrieve_note(note_id: int, service: NoteServices = Depends(NoteServices)):
    note = await service.retrieve(note_id)

    return note


@router.patch("/notes/{id}", tags=['Notes'], status_code=204)
async def update_note(note_id: int, input_schema: NoteOut, service: NoteServices = Depends(NoteServices)):
    result = await service.update(note_id, input_schema)


@router.delete("/notes/{id}", tags=['Notes'], status_code=204)
async def delete_note(note_id: int, service: NoteServices = Depends(NoteServices)):
    result = await service.delete(note_id)


@router.post("/notes/{id}/done", tags=['Notes'])
async def mark_note_done(note_id: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_done(note_id)


@router.post("/notes/{id}/undone", tags=['Notes'])
async def mark_note_undone(note_id: int, service: NoteServices = Depends(NoteServices)):
    result = await service.mark_note_undone(note_id)
