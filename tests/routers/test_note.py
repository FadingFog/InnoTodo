from app.schemas.note import NoteOut


async def test_create_note_create_and_return_note(client, router):
    url = "/api" + router.url_path_for("create_note")
    data = {"list_id": 1, "text": "test_text"}
    response = client.post(url, json=data)

    assert response.status_code == 200
    assert data.items() <= response.json().items()


async def test_create_note_return_422_if_scheme_not_valid(client, router):
    url = "/api" + router.url_path_for("create_note")
    data = {}
    response = client.post(url, json=data)

    assert response.status_code == 422


async def test_retrieve_note_return_note(client, router, note: NoteOut):
    url = "/api" + router.url_path_for("retrieve_note", pk=note.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == note.dict()


async def test_retrieve_note_return_404_if_note_not_exists(client, router):
    url = "/api" + router.url_path_for("retrieve_note", pk=1)
    response = client.get(url)

    assert response.status_code == 404


async def test_update_note_return_204_if_updated(client, router, note: NoteOut):
    url = "/api" + router.url_path_for("update_note", pk=note.id)
    data = {"text": "test_text"}
    response = client.patch(url, json=data)

    assert response.status_code == 204


async def test_update_note_return_404_if_note_not_exists(client, router):
    url = "/api" + router.url_path_for("update_note", pk=1)
    data = {"text": "test_text"}
    response = client.patch(url, json=data)

    assert response.status_code == 404


async def test_delete_note_return_204_if_deleted(client, router, note: NoteOut):
    url = "/api" + router.url_path_for("delete_note", pk=note.id)
    response = client.delete(url)

    assert response.status_code == 204


async def test_delete_note_return_404_if_note_not_exists(client, router):
    url = "/api" + router.url_path_for("delete_note", pk=1)
    response = client.delete(url)

    assert response.status_code == 404


async def test_mark_note_done_return_200_if_successful(client, router, note: NoteOut):
    url = "/api" + router.url_path_for("mark_note_done", pk=note.id)
    response = client.post(url)

    assert response.status_code == 200


async def test_mark_note_done_return_404_if_note_not_exists(client, router):
    url = "/api" + router.url_path_for("mark_note_done", pk=1)
    response = client.post(url)

    assert response.status_code == 404


async def test_mark_note_undone_return_200_if_successful(client, router, note: NoteOut):
    url = "/api" + router.url_path_for("mark_note_undone", pk=note.id)
    response = client.post(url)

    assert response.status_code == 200


async def test_mark_note_undone_return_404_if_note_not_exists(client, router):
    url = "/api" + router.url_path_for("mark_note_done", pk=1)
    response = client.post(url)

    assert response.status_code == 404
