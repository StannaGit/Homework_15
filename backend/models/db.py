'''
Модель бази даних - для зберігання структури даних "студент":
використовується вбудована БД Sqlite Python
https://www.tutorialspoint.com/sqlite/sqlite_python.htm
https://docs.python.org/3/library/sqlite3.html
'''


from infra.database import ORM_DATABASE as db

# опис бази даних "library"
class BooksDBModel(db.Model):
    __tablename__ = "books"

    # опис полів бази даних "library"
    books_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    books_name: str = db.Column(db.String(200))
    author: str = db.Column(db.String(200))
    year_creat: int = db.Column(db.Integer)

    def __init__(
        self,
        books_name: str,
        author: str,
        year_creat: int
    ) -> None:
        self.books_name = str(books_name)
        self.author = str(author)
        self.year_creat = int(year_creat)
