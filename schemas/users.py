from pydantic import BaseModel, validator
from db import SessionLocal

db = SessionLocal()


class CreateUser(BaseModel):
    name: str
    username: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password


class UpdateUser(BaseModel):
    name: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password


class CreateGeneralUser(BaseModel):
    name: str
    username: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password
