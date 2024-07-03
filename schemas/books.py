from datetime import date

from pydantic import BaseModel, ConfigDict


class CreateBooks(BaseModel):
    name: str
    author: str
    date: date
    isbn: str
    genre: str
    language: str
    publisher: str
    pages: int
    description: str
    count: int
    price: int
    discount: float
    discount_time: date
    rating: int

    model_config = ConfigDict(arbitrary_types_allowed=True)


class UpdateBooks(BaseModel):
    ident: int
    name: str
    author: str
    date: date
    isbn: str
    genre: str
    language: str
    publisher: str
    pages: int
    description: str
    count: int
    price: int
    discount: float
    discount_time: date
    rating: int

    model_config = ConfigDict(arbitrary_types_allowed=True)