from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models import AuthorModel, BookModel
from app.schemas import Author, BaseAuthor, CreateAuthor, BaseBook, CreateBook, BaseModel, Book
from app.database import SessionLocal, Base
from app.crud import author_list, author_create, author_delete, author_update, book_list, book_create, book_delete, book_update

app = FastAPI()


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


# READ
@app.get("/authors/{author_id}", response_model=Author)
def get_author(author_id: int):
    db = SessionLocal()
    author = db.query(AuthorModel).filter(AuthorModel.id == author_id).first()
    db.close()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db.close()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# CREATE
@app.post("/authors/", response_model=Author)
def create_author(author: CreateAuthor):
    db = SessionLocal()
    author_model = AuthorModel(**author.model_dump())
    db.add(author_model)
    db.commit()
    db.refresh(author_model)
    db.close()
    return author_model


@app.post("/books/", response_model=Book)
def create_book(book: CreateBook):
    db = SessionLocal()
    book_model = BookModel(**book.model_dump())
    db.add(book_model)
    db.commit()
    db.refresh(book_model)
    db.close()
    return book_model


# UPDATE
@app.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: CreateAuthor):
    db = SessionLocal()
    author_model = db.query(AuthorModel).filter(AuthorModel.id == author_id).first()
    if author_model is None:
        db.close()
        raise HTTPException(status_code=404, detail="Author not found")
    for key, value in author.model_dump().items():
        setattr(author_model, key, value)
    db.commit()
    db.close()
    return author_model


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: CreateBook):
    db = SessionLocal()
    book_model = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book_model is None:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(book_model, key, value)
    db.commit()
    db.close()
    return book_model


# DELETE
@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    db = SessionLocal()
    author_model = db.query(AuthorModel).filter(AuthorModel.id == author_id).first()
    if author_model is None:
        db.close()
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author_model)
    db.commit()
    db.close()
    return {"message": "Author deleted successfully"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    book_model = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book_model is None:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book_model)
    db.commit()
    db.close()
    return {"message": "Book deleted successfully"}





"""@app.get("/")
async def get_author_info(id: int | None = None, name: str | None = None, books: str | None = None, db: Session = Depends(get_db)):
    filter_emp = Author

    if id is not None:
        filter_emp = list(filter(lambda x: x['age'] == id, Author))
    if name is not None:
        filter_emp = list(filter(lambda x: x['salary'] == name, Author))
    if books is not None:
        filter_emp = list(filter(lambda x: x['is_active'] == books, Author))

    return {'filter_emp': filter_emp}


@app.get("/users/{author_id}")
async def search_author(author_id: int):
    # Пошук користувача за id
    employee = list(filter(lambda x: x['id'] == author_id, Author))

    if employee is None:
        # Якщо користувач не знайдений, підняти HTTPException з кодом 404
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"author_index": employee}


@app.post("/users/create")
async def create_employees(author: Author):
    return Author.model_dump(author)


@app.put("/users/{user_id}")
async def update_user(author_id: int, updated_author: Author):
    # Пошук користувача за id
    author_index = next((index for index, emp in enumerate(Author) if emp['id'] == author_id), None)

    if author_index is not None:
        # Оновлення користувача за індексом
        Author[author_index].update(updated_author)
        return {"message": "User updated successfully"}
    else:
        # Якщо користувач не знайдений, підняти HTTPException з кодом 404
        raise HTTPException(status_code=404, detail="Author not found")
"""