import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import scoped_session

from app.config import settings
from app.models import Base

engine = create_async_engine(settings.TEST_DATABASE_URL)

async_session = async_sessionmaker(engine, class_=AsyncSession, autocommit=False, expire_on_commit=False, autoflush=True)
sc_session = scoped_session(async_session)  # noqa


@pytest.fixture(scope='function', autouse=True)
async def recreate_tables() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def db_session_impl() -> AsyncSession:
    async with engine.begin() as connection:
        async with async_session(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()


@pytest.fixture
async def db_session() -> AsyncSession:
    agen = db_session_impl()

    async for session in agen:
        yield session


from tests.fixtures import *  # noqa
