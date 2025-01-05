'''
Модуль підключення до бази даних Sqlite Python - фізичне її створення.
Це локальна БД.
'''

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME: str = os.path.join(os.getcwd(), "books.db")        # "фізична" побудова БД в кореневому для api каталозі
CONNECTION_STRING: str = f"sqlite:///{DB_NAME}"

'''
БД може зберігатись на іншому сервері, тоді CONNECTION_STRING буде мати посмлання на неї + пароль доступу
'''

ORM_DATABASE = None


def init_db(app: Flask):
    global ORM_DATABASE

    app.config["SQLALCHEMY_DATABASE_URI"] = CONNECTION_STRING   # побудова полів БД
    app.config["SECRET_KEY"] = "sUpeRSecr3t!Str1ng"             # захист полів бази даних за SECRET_KEY - бажано мати рандомні паролі

    ORM_DATABASE = SQLAlchemy(app)

    # do not remove imports, they are used implicitly
    from models.db import BooksDBModel

    with app.app_context():
        ORM_DATABASE.create_all()

