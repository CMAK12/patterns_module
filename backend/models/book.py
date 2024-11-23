from sqlalchemy import Column, Integer, String, Text, Uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Uuid, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=True)

