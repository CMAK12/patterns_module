from sqlalchemy import delete, update
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from db.database import database
from models.book import Book
from schemas.book_schema import BookCreate, BookUpdate
from sqlalchemy.future import select

class BookRepository:
    async def get_books(self):
        async with database.get_session() as session:
            result = await session.execute(select(Book))
            return result.scalars().all()

    async def get_book(self, book_id: UUID):
        async with database.get_session() as session:
            result = await session.execute(select(Book).where(Book.id == book_id))
            book = result.scalar_one_or_none()
            if not book:
                raise NoResultFound("Book not found")
            return book

    async def create_book(self, book_data: Book):
        async with database.get_session() as session:
            session.add(book_data)
            await session.commit()
            return book_data

    async def update_book(self, book_id: UUID, book_data: BookUpdate):
        async with database.get_session() as session:
            await session.execute(
                update(Book)
                .where(Book.id == book_id)
                .values(**{k: v for k, v in book_data.dict(exclude_unset=True).items()})
            )
            await session.commit()
            return book_data

    async def delete_book(self, book_id: UUID):
        async with database.get_session() as session:
            await session.execute(delete(Book).where(Book.id == book_id))
            await session.commit()
            return True