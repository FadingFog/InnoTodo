from app.models import Note
from app.repositories.base import BaseRepository


class NoteRepository(BaseRepository):
    model = Note
