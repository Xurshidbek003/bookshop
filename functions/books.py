from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.books import Books


def get_book(name, genre, price, author, rating, page, limit, db):
    query = db.query(Books)
    if name:
        query = query.filter(Books.name.ilike(f"%{name}%"))
    if genre:
        query = query.filter(Books.genre.ilike(f"%{genre}%"))
    if price:
        query = query.filter(Books.price < price)
    if author:
        query = query.filter(Books.author.ilike(f"%{author}%"))
    if rating:
        query = query.filter(Books.rating == rating)

    items = query.all()
    return pagination(items, page, limit)


def create_book(forms, db):
    for form in forms:
        new_item_db = Books(
            name=form.name,
            author=form.author,
            date=form.date,
            isbn=form.isbn,
            genre=form.genre,
            language=form.language,
            publisher=form.publisher,
            pages=form.pages,
            description=form.description,
            count=form.count,
            price=form.price,
            discount=form.discount,
            discount_time=form.discount_time,
            discount_price=form.price - (form.price * form.discount) / 100,
            rating=form.rating
        )
        save_in_db(db, new_item_db)


def update_book(forms, db):
    for form in forms:
        get_in_db(db, Books, form.ident)
        db.query(Books).filter(Books.id == form.ident).update({
            Books.name: form.name,
            Books.author: form.author,
            Books.date: form.date,
            Books.isbn: form.isbn,
            Books.genre: form.genre,
            Books.language: form.language,
            Books.publisher: form.publisher,
            Books.pages: form.pages,
            Books.description: form.description,
            Books.count: form.count,
            Books.price: form.price,
            Books.discount: form.discount,
            Books.discount_time: form.discount_time,
            Books.discount_price: form.price - (form.price * form.discount) / 100,
            Books.rating: form.rating
        })
    db.commit()


def delete_book(ident, db):
    get_in_db(db, Books, ident)
    db.query(Books).filter(Books.id == ident).delete()
    db.commit()
