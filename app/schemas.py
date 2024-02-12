from pydantic import BaseModel


class BaseAuthor(BaseModel):
    name: str
    age: int


class CreateAuthor(BaseAuthor):
    pass


class Author(BaseAuthor):
    id: int

    class Config:
        orm_mode = True


class BaseBook(BaseModel):
    title: str
    description: str
    published_year: int
    price: int
    author_id: int


class CreateBook(BaseBook):
    pass


class Book(BaseBook):
    id: int

    class Config:
        orm_mode = True





