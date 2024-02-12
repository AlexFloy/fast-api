from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

    books = relationship('BookModel', back_populates='author')


class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    published_year = Column(Integer)
    price = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('AuthorModel', back_populates='books')

    class Config:
        orm_mode = True
