from db import Base
from sqlalchemy import Column, String, Integer, Date, Float


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    date = Column(Date)
    isbn = Column(String(255), nullable=False)
    genre = Column(String(255), nullable=False)
    language = Column(String(255), nullable=False)
    publisher = Column(String(255), nullable=False)
    pages = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    count = Column(Integer, nullable=True)
    price = Column(String(255), nullable=False)
    discount = Column(Float, nullable=True)
    discount_time = Column(Date, nullable=True)
    discount_price = Column(Integer, nullable=True)
    rating = Column(String(255), nullable=True)
