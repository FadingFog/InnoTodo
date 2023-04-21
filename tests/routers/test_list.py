from app.schemas.list import ListOut
from app.schemas.note import NoteOut


async def test_create_list_create_and_return_list(client, router):
    url = "/api" + router.url_path_for("create_list")
    data = {"title": "test_title"}
    response = client.post(url, json=data)

    assert response.status_code == 200
    assert data.items() <= response.json().items()


async def test_create_list_return_422_if_scheme_not_valid(client, router):
    url = "/api" + router.url_path_for("create_list")
    data = {}
    response = client.post(url, json=data)

    assert response.status_code == 422


async def test_retrieve_list_return_list(client, router, list_todo: ListOut):
    url = "/api" + router.url_path_for("retrieve_list", pk=list_todo.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == list_todo.dict()


async def test_retrieve_list_return_404_if_list_not_exists(client, router):
    url = "/api" + router.url_path_for("retrieve_list", pk=1)
    response = client.get(url)

    assert response.status_code == 404


async def test_retrieve_list_with_notes_return_list_with_notes(client, router, note: NoteOut):
    url = "/api" + router.url_path_for("retrieve_list_with_notes", pk=note.list_id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["notes"][0] == note.dict()


async def test_retrieve_list_with_notes_return_404_if_list_not_exists(client, router):
    url = "/api" + router.url_path_for("retrieve_list_with_notes", pk=1)
    response = client.get(url)

    assert response.status_code == 404


async def test_retrieve_user_lists_return_user_lists(client, router, list_todo: ListOut):
    url = "/api" + router.url_path_for("retrieve_user_lists", pk=list_todo.owner_id)
    response = client.get(url)

    assert response.status_code == 200
    assert list_todo.dict() in response.json()


async def test_retrieve_user_lists_return_empty_list_if_user_not_exists(client, router):
    url = "/api" + router.url_path_for("retrieve_user_lists", pk=1)
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 0


async def test_update_list_return_204_if_updated(client, router, list_todo: ListOut):
    url = "/api" + router.url_path_for("update_list", pk=list_todo.id)
    data = {"title": "test_title"}
    response = client.patch(url, json=data)

    assert response.status_code == 204


async def test_update_list_return_404_if_list_not_exists(client, router):
    url = "/api" + router.url_path_for("update_list", pk=1)
    data = {"title": "test_title"}
    response = client.patch(url, json=data)

    assert response.status_code == 404


async def test_delete_list_return_204_if_deleted(client, router, list_todo: ListOut):
    url = "/api" + router.url_path_for("delete_list", pk=list_todo.id)
    response = client.delete(url)

    assert response.status_code == 204


async def test_delete_list_return_404_if_list_not_exists(client, router):
    url = "/api" + router.url_path_for("delete_list", pk=1)
    response = client.delete(url)

    assert response.status_code == 404
