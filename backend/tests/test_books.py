from http.client import responses

from alembic.util import not_none
from fastapi.testclient import TestClient
from uuid import UUID

import builders.book_builder
import db.database
import schemas.book_schema
from main import app
from models.book import Book

client = TestClient(app)

def test_create_book():
    response = client.post("/api/book/", json={
        "title": "Test Book",
        "author": "Author Name",
        "description": "A description",
        "published_year": 2023
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_is_database_singlton():
    db1 = db.database.database.__hash__()
    db2 = db.database.database.__hash__()
    assert db1 == db2

def test_builder():
    bookBuilder = builders.book_builder.BookBuilder()
    book = bookBuilder \
        .set_title("Test Book") \
        .set_author("Author Name") \
        .set_description("A description") \
        .set_published_year(2023) \
        .build()
    assert not_none(book)
    assert isinstance(book.id, UUID)
    assert isinstance(book, Book)

