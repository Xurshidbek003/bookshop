import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import database
from functions.books import get_book, create_book, update_book, delete_book
from routes.login import get_current_active_user
from schemas.books import CreateBooks, UpdateBooks
from schemas.users import CreateUser
from utils.role_verification import role_verification

books_router = APIRouter(
    prefix="/books",
    tags=["Books operation"]
)


@books_router.get('/get')
def get_books(name: str = None, genre: str = None, price: int = 0, author: str = None, rating: int = 0,
              page: int = 1, limit: int = 25, db: Session = Depends(database)):
    return get_book(name, genre, price, author, rating, page, limit, db)


@books_router.post('/create')
def create_books(forms: List[CreateBooks], db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_book(forms, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@books_router.put("/update")
def update_books(forms: List[UpdateBooks], db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_book(forms, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@books_router.delete("/delete")
def delete_books(ident: int = 0, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_book(ident, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
