from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from core.config import settings
from asyncio import current_task


class DatabaseHelper:
    def __init__(self, url: str) -> None:
        self.engine = create_async_engine(
            url=url,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def get_async_session(self):
        async with self.session_factory() as session:
            yield session

    async def session_dependency(self) -> AsyncGenerator:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncGenerator:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(url=settings.db_url)
