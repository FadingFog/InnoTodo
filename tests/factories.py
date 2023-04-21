import factory
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory
from factory import fuzzy, SubFactory

from app.models import ListTodo, Note
from tests.conftest import sc_session


class ListTodoFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = ListTodo
        sqlalchemy_session = sc_session

    title = fuzzy.FuzzyText()
    owner_id = factory.Sequence(lambda n: n + 1)


class NoteFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Note
        sqlalchemy_session = sc_session

    text = fuzzy.FuzzyText()
    list = SubFactory(ListTodoFactory)
