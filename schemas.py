from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_joined: str | None = None
    age: int
    city: str | None = None
    library_id: str | None = None
    is_active: bool
    salary: int
