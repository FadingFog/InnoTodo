from app.schemas.list import ListOut


async def test_get_by_id_return_obj(list_repo, list_todo: ListOut):
    result_orm = await list_repo.get_by_id(list_todo.id)
    result = ListOut.from_orm(result_orm)

    assert result == list_todo


async def test_get_by_id_return_none_if_obj_not_exists(list_repo):
    result = await list_repo.get_by_id(1)

    assert result is None


async def test_get_one_by_field_return_obj(list_repo, list_todo: ListOut):
    result_orm = await list_repo.get_one_by_field("owner_id", list_todo.owner_id)
    result = ListOut.from_orm(result_orm)

    assert result == list_todo


async def test_get_one_by_field_return_none_if_obj_not_exists(list_repo):
    result = await list_repo.get_one_by_field("owner_id", 1)

    assert result is None


async def test_get_one_by_field_return_none_if_field_not_exists(list_repo, list_todo: ListOut):
    result = await list_repo.get_one_by_field("test", "test")

    assert result is None


async def test_get_all_by_field_return_list_of_objects(list_repo, list_todo: ListOut, create_list_todo):
    list_todo_2 = await create_list_todo(values={"owner_id": 1})
    list_todo_3 = await create_list_todo(values={"owner_id": 1})

    result = await list_repo.get_all_by_field("owner_id", 1)

    assert len(result) == 2
    for obj in result:
        assert obj.owner_id == 1


async def test_get_all_by_field_return_empty_list_if_objects_not_exists(list_repo, list_todo: ListOut):
    result = await list_repo.get_all_by_field("owner_id", 1)

    assert len(result) == 0


async def test_get_all_by_field_return_empty_list_if_field_not_exists(list_repo, list_todo: ListOut):
    result = await list_repo.get_all_by_field("test", "test")

    assert len(result) == 0


async def test_get_all_return_list_of_objects(list_repo, list_todo: ListOut):
    result = await list_repo.get_all()

    assert len(result) == 1
    assert list_todo == ListOut.from_orm(result[0])


async def test_get_all_return_empty_list_if_objects_not_exists(list_repo):
    result = await list_repo.get_all()

    assert len(result) == 0


async def test_create_create_obj(list_repo, create_list_todo):
    list_todo = await create_list_todo(add=False)
    objects = await list_repo.get_all()
    assert not objects

    created_obj = await list_repo.create(list_todo)
    objects = await list_repo.get_all()

    assert len(objects) == 1
    assert ListOut.from_orm(objects[0]) == ListOut.from_orm(list_todo)


async def test_create_return_obj(list_repo, create_list_todo):
    list_todo = await create_list_todo(add=False)

    created_obj = await list_repo.create(list_todo)

    assert created_obj == list_todo


async def test_create_return_error_if_obj_with_unique_values_already_exists(list_repo):
    ...  # raise NotImplementedError


async def test_update_update_obj(list_repo, list_todo: ListOut):
    old_title = list_todo.title

    result = await list_repo.update(list_todo.id, {"title": "new_title"})
    updated_obj = await list_repo.get_by_id(list_todo.id)

    assert updated_obj.title != old_title
    assert updated_obj.title == "new_title"


async def test_update_return_result(list_repo, list_todo: ListOut):
    result = await list_repo.update(list_todo.id, {"title": "new_title"})

    assert result.rowcount > 0


async def test_update_return_empty_result_if_obj_not_exists(list_repo):
    result = await list_repo.update(1, {"title": "new_title"})

    assert result.rowcount == 0


async def test_delete_return_delete_obj(list_repo, list_todo: ListOut):
    _ = await list_repo.delete(list_todo.id)
    result = await list_repo.get_by_id(list_todo.id)

    assert not result


async def test_delete_return_result(list_repo, list_todo: ListOut):
    result = await list_repo.delete(list_todo.id)

    assert result.rowcount > 0


async def test_delete_return_empty_result_if_obj_not_exists(list_repo):
    result = await list_repo.delete(1)

    assert result.rowcount == 0
