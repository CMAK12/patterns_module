from repositories.book_repository import BookRepository
from schemas.book_schema import BookCreate, BookUpdate
from uuid import UUID
from models.book import Book

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    async def add_book(self, book: Book):
        return await self.repository.create_book(book)

    async def list_books(self):
        return await self.repository.get_books()

    async def get_book(self, book_id: UUID):
        return await self.repository.get_book(book_id)

    async def update_book(self, book_id: UUID, book_data: BookUpdate):
        return await self.repository.update_book(book_id, book_data)

    async def delete_book(self, book_id: UUID):
        return await self.repository.delete_book(book_id)
