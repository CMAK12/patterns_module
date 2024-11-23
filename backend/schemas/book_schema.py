from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str]
    published_year: Optional[int]

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = None

class BookRead(BookBase):
    id: UUID

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True