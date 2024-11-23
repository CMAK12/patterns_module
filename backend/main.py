from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from builders.book_builder import BookBuilder
from services.book_service import BookService
from schemas.book_schema import BookCreate, BookRead, BookUpdate

app = FastAPI()
book_service = BookService()

app.add_middleware(
    CORSMiddleware,
    allow_origins='http://127.0.0.1:5500',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/book/", response_model=BookRead)
async def create_book(book_data: BookCreate):
    builder = BookBuilder()
    book = builder \
        .set_title(book_data.title) \
        .set_author(book_data.author) \
        .set_description(book_data.description) \
        .set_published_year(book_data.published_year) \
        .build()

    return await book_service.add_book(book)

@app.get("/api/book/", response_model=list[BookRead])
async def read_books():
    return await book_service.list_books()

@app.get("/api/book/{book_id}", response_model=BookRead)
async def read_book(book_id: UUID):
    try:
        return await book_service.get_book(book_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Book not found")

@app.put("/api/book/{book_id}", response_model=BookUpdate)
async def update_book(book_id: UUID, book: BookUpdate):
    try:
        return await book_service.update_book(book_id, book)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/api/book/{book_id}", response_model=dict)
async def delete_book(book_id: UUID):
    try:
        await book_service.delete_book(book_id)
        return {"detail": "Book deleted"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Book not found")