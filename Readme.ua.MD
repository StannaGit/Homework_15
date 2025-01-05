# Застосунок "Список студентів"

## Запуск локально

### Запуск python бекенду

- Створіть віртуальне оточення python venv та активуйте його
    ```python
    > python -m venv venv
    > source venv/bin/activate
    ```
- Перейдіть в папку backend
    ```shell
    (venv) > cd backend
    ```
- Встановіть python залежності за допомогою pip:
    ```
    (venv) ..backend > pip install -r requirements.txt
    ```
- Запуск Flask застосунку:
    ```python
    (venv) ..backend > python app.py
    ```
Приблизний результат запуску у вікні виводу:
```shell
* Serving Flask app 'app'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Запуск javascript фронтенд застосунку

- Завантажте [nodejs](https://nodejs.org/en/download/) з офіційного сайту
- Після завершення інсталяції перевірте наявність npm:
    ```
    > npm --version
    ```
- Перейдіть у папку `frontend/client`:
    ```
    > cd frontend/client
    ```
- Встановіть залежності для фронтенду за допомогою npm:
    ```
    > npm install
    ```
    Дочекайтесь завершення завантаження пакетів

- Спробуйте запустити застосунок:
    ```
    > npm run serve
    ```
- Якщо застосунок не запустився спробуйте виконати запуск таким чином:
    - Linux:
    ```
    > export NODE_OPTIONS=--openssl-legacy-provider
    > npm run serve
    ```
    - Windows:
    ```
    > set NODE_OPTIONS=--openssl-legacy-provider
    > npm run serve
    ```