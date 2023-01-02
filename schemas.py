from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90,
                     description="Возраст автора не может быть меньше 15 лет и больше 90")

    # @validator('age')
    # def check_age(cls, value):
    #    if 15 < value < 90:
    #        raise ValueError('Возраст автора не может быть меньше 15 лет')
    #    return value


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int = 100

class BookOut(Book):
    id: int = 1
