'''
Комплект необхідних для роботи фреймворка Flask інструментів:
Flask - фреймворк для створення WEB-застосунків
Flask-CORS - розширення Flask для керування спільним використанням ресурсів із перехресним джерелом
flask-sqlalchemy - робота із базою даних
flask-restful - для швидкого створення WEB API
flask-restful-swagger - генерування стандартної документації / огортки для API

Створення проекту Flask:
https://flask.palletsprojects.com/en/3.0.x/tutorial/layout/
https://realpython.com/flask-blueprint/
https://realpython.com/flask-project/

'''


# !!! усі встановлення / налаштування по бібліотеках та фреймворка - слід робити ТІЛЬКИ у віртуальному оточенні

from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_restful_swagger import swagger

from infra.database import init_db


# створення Flask застосунку - конфігурування налаштувань фреймворка Flask для бізнес вимог застосунку:
app = Flask(__name__)                               # створення екземпляр класу Flask
app.url_map.strict_slashes = False                  # підключає правило URL
api = swagger.docs(Api(app), apiVersion='0.1')      # створення обєкту api + документація для нього - стандартизований json файл для розробників Frontend
CORS(app, resources={r"/*": {"origins": "*"}})      # увімкнути CORS (дозволити міжсайтові запити)


# фреймворк Flask має багато рішень на типові потреби із створення WEB-застосунків
'''
Приклад запитів на уточнення налаштувань фреймворка Flask:
як додати аутентифікацію на Flask:
https://flask-login.readthedocs.io/en/latest/
https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/
як додати двохрівневу авторизацію на Flask:
https://flask-security-too.readthedocs.io/en/stable/two_factor_configurations.html
'''

# створення ресурсу локального серверу за допомогою  from flask_restful import Api, Resource
# формування запиту get з відповіддю Hello, World!!
class HelloWorld(Resource):
    def get(self):
        return "Hello, World !!!"


api.add_resource(HelloWorld, "/")           # поточна адреса локального WEB-сервера
# api.add_resource(HelloWorld, "/6")


if __name__ == "__main__":
    
    # створення БД студентів
    init_db(app)


    from api.books_api import BookList, Book
    api.add_resource(BookList, "/books")
    api.add_resource(Book, "/books/<int:book_id>")

    # виклик локального серверу
    app.run(debug=True)                 # налаштування локального WEB-сервера в api
    # app.run()                         # налаштування локального WEB-сервера в api

    '''
    Результат:
    * Serving Flask app 'app'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000          "зарезервований хост власного вузла (5000 порт) - локальний WEB-сервер"
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 114-012-699  
    
    '''
