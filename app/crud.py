from sqlalchemy.orm import Session

from app.schemas import CreateBook, CreateAuthor, BaseBook, Book, BaseAuthor, Author
from app.models import AuthorModel, BookModel


def book_list(db: Session):
    return db.query(BookModel).all()


def book_create(db: Session, book: CreateBook):
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def book_delete(db: Session, book_id: int):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book:
        db.delete(db_book)
        db.commit()
        db.refresh(db_book)
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}


def book_update(db: Session, book: BookModel):
    db_book = db.query(BookModel).filter(Book.id == book.id).first()

    if db_book:
        db_book.title = book.title
        db_book.description = book.description
        db_book.published_year = book.published_year
        db_book.price = book.price
        db_book.author_id = book.author_id

        db.commit()
        db.refresh(db_book)
        return {"message": "Book updated successfully"}
    else:
        return {"error": "Book not found"}


def author_list(db: Session):
    return db.query(AuthorModel).all()


def author_create(db: Session, author: CreateAuthor):
    db_author = AuthorModel(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def author_delete(db: Session, author_id: int):
    db_author = db.query(AuthorModel).filter(AuthorModel.id == author_id).first()

    if db_author:
        db.delete(db_author)
        db.commit()
        db.refresh(db_author)
        return {"message": "Author deleted successfully"}
    else:
        return {"error": "Author not found"}


def author_update(db: Session, author: BaseAuthor):
    db_author = db.query(BaseAuthor).filter(Author.id == author.id).first()

    if db_author:
        db_author.name = author.name
        db_author.age = author.age

        db.commit()
        db.refresh(db_author)
        return {"message": "Author updated successfully"}

    else:
        return {"error": "Author not found"}
