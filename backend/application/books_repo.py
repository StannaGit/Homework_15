'''
Модуль - бізнес модель - застосування БД - робота з полями БД
Логіка може бути будь-яка, на ВАШУ думку.
Пу суті - маємо сценарій дій / операцій над структурою даних "студент"

'''

from typing import Tuple

from infra.database import ORM_DATABASE
from models.dto import BooksDTO
from models.db import BooksDBModel


class BooksRepository:
    
    @classmethod
    def get_all_books(cls) -> tuple[BooksDTO]:                     # отримати усіх студентів з БД
        db_result = BooksDBModel.query.all()                          # метод .query.all - забезпечує доступ до полів моделі БД
        result = []
        for db_row in db_result:                                        # type : BooksDBModel - генератор
            result.append(
                BooksDTO(
                    books_id=db_row.books_id,
                    books_name=db_row.books_name,
                    author=db_row.author,
                    year_creat=db_row.year_creat,
                )
            )

        return tuple(result)                                            # результат повертаїмо в кортежі: упорядкована незмінна колекція

    @classmethod
    def get_book_by_id(cls, books_id: int) -> BooksDTO:          # отримати з БД студента за id
        db_row = BooksDBModel.query.filter_by(books_id=books_id).first()
        if not db_row:
            raise ValueError(f"Not found book {books_id}")

        return BooksDTO(
            books_id=db_row.books_id,
            books_name=db_row.books_name,
            author=db_row.author,
            year_creat=db_row.year_creat,
        )

    @classmethod
    def insert_new_book(cls, book_data: dict) -> bool:             # додати нового студента
        new_book = BooksDBModel(**book_data)

        try:
            ORM_DATABASE.session.add(new_book)
            ORM_DATABASE.session.commit()
            return True
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return False

    @classmethod
    def update_book_by_id(cls, books_id: int, data: dict) -> bool: # модифікувати інформацію про студента з id
        try:
            result = ORM_DATABASE.session.query(BooksDBModel).filter(
                BooksDBModel.books_id == books_id
            ).update(data)

            if not result:
                ORM_DATABASE.session.rollback()
                return False
            
            ORM_DATABASE.session.commit()
            return True
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return False

    @classmethod
    def delete_book_by_id(cls, books_id: int) -> Tuple[BooksDTO, bool]:  # видалити інформацію про студента з id
        try:
            db_row = BooksDBModel.query.filter_by(books_id=books_id).first()
            if not db_row:
                raise ValueError(f"Not found book with Id {books_id}")

            deleted_book = BooksDTO(
                books_id=db_row.books_id,
                books_name=db_row.books_name,
                author=db_row.author,
                year_creat=db_row.year_creat,
            )
            ORM_DATABASE.session.query(BooksDBModel).filter(
                BooksDBModel.books_id == books_id
            ).delete()

            ORM_DATABASE.session.commit()
            return deleted_book, True
        except ValueError:
            raise
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return None, False
