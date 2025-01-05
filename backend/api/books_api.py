'''
Модуль представлення БД - репозиторію студентів booksRepository

'''

from http import HTTPStatus

from flask import request, jsonify, Response, make_response
from flask_restful import Resource                              # бібліотека роботи з ресурсами - для створення їх api

from application.books_repo import BooksRepository


books_repo = BooksRepository


class BookList(Resource):                                    # репрезентація ресурсу список студентів
    def get(self) -> Response:                                  # отримати список всіх студентів - http_calls - books.http
        return jsonify(books_repo.get_all_books())

    def post(self) -> Response:
        result = books_repo.insert_new_book(request.get_json())   # додати нового студента

        if not result:
            return make_response(jsonify("Failed to insert!"), HTTPStatus.INTERNAL_SERVER_ERROR)

        return make_response(jsonify("Created"), HTTPStatus.CREATED)


class Book(Resource):                                        # репрезентація ресурсу студент
    def get(self, book_id: int) -> Response:                 # отримати дані студента
        return make_response(jsonify(books_repo.get_book_by_id(book_id)), HTTPStatus.OK)

    def put(self, book_id: int) -> Response:                 # змінити дані студента

        try:
            is_success = books_repo.update_book_by_id(
                book_id= book_id,
                data=request.get_json(),
            )

            if not is_success:
                return make_response(f"book failed to update", HTTPStatus.INTERNAL_SERVER_ERROR)

            return make_response(f"book updated!", HTTPStatus.OK)

        except ValueError as ex:
            print(ex)
            return make_response(f"book not found", HTTPStatus.NOT_FOUND)
        except Exception as err:
            print(err)
            return make_response(f"Error updating book -> {err}", HTTPStatus.INTERNAL_SERVER_ERROR)

    def delete(self, book_id: int) -> Response:                 # видалити дані студента
        try:
            deleted_book, is_success = books_repo.delete_book_by_id(
                book_id=book_id,
            )
            
            if not is_success:
                return make_response(
                    f"Failed to delete book with ID {book_id}",
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )

            return make_response(
                f"book {deleted_book.books_name} {deleted_book.author} deleted!",
                HTTPStatus.OK,
            )
        except ValueError as ex:
            print(ex)
            return make_response(f"book not found", HTTPStatus.NOT_FOUND)

