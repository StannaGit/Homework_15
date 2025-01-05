# books List Application

## Local Run

### Run python app

- Create virtual environment and activate it
    ```python
    > python -m venv venv
    > source venv/bin/activate
    ```
- cd to backend directory
    ```shell
    (venv) > cd backend
    ```
- install all dependencies:
    ```
    (venv) ..backend > pip install -r requirements.txt
    ```
- run Flask application:
    ```python
    (venv) ..backend > python app.py
    ```
You should have something similar to this:
```shell
* Serving Flask app 'app'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Run javascript frontend app

- Download [nodejs](https://nodejs.org/en/download/) from official website 
- Once finished check npm installation:
    ```
    > npm --version
    ```
- CD to `frontend/client` directory:
    ```
    > cd frontend/client
    ```
- Install 3rd party packages using npm:
    ```
    > npm install
    ```
    Wait for the progress it will download

- Try to run the app:
    ```
    > npm run serve
    ```
- If the application didn't start do the following:
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