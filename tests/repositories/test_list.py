from app.schemas.list import ListOutWithNotes
from app.schemas.note import NoteOut


async def test_get_by_id_with_notes_return_list_with_notes(list_repo, note: NoteOut):
    result_orm = await list_repo.get_by_id_with_notes(note.list_id)
    result = ListOutWithNotes.from_orm(result_orm)

    assert note in result.notes


async def test_get_by_id_with_notes_return_none_if_list_not_exists(list_repo):
    result_orm = await list_repo.get_by_id_with_notes(1)

    assert result_orm is None


async def test_get_by_id_with_notes_return_list_with_empty_notes_list_if_notes_not_exists(list_repo, list_todo: ListOutWithNotes):
    result_orm = await list_repo.get_by_id_with_notes(list_todo.id)
    result = ListOutWithNotes.from_orm(result_orm)

    assert len(result.notes) == 0
