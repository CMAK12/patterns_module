from random import randint
from uuid import uuid4

from models.book import Book

class BookBuilder:
    def __init__(self):
        self._id = None
        self._title = None
        self._author = None
        self._description = None
        self._published_year = None

    def set_title(self, title: str):
        self._title = title
        return self

    def set_author(self, author: str):
        self._author = author
        return self

    def set_description(self, description: str):
        self._description = description
        return self

    def set_published_year(self, published_year: int):
        self._published_year = published_year
        return self

    def build(self) -> Book:
        return Book(
            id=uuid4(),
            title=self._title,
            author=self._author,
            description=self._description,
            published_year=self._published_year
        )
