Flask-Intro
===========

Sample code from my "Introduction to Flask" presentation. The slides for this presentation are available at [https://speakerdeck.com/miguelgrinberg/introduction-to-flask](https://speakerdeck.com/miguelgrinberg/introduction-to-flask).


Repositories
------------
- Migrate

Requirements
------------

- flask-logging:
- flask-celery:
- flask-login-decorator:
- flask-migrate: app example to demonstrate the migrations steps using alembic
- flask-pymongo: app exmple to demostrate how to connectioon in mongo db using flask
- flask-redis: app that show the use of redis in a simple way
- flask-rest-sqlite: a simple rest app builded using sqlite
- flask-session: controling sessions
- flask-sqlite: database for sqlite


flask-api: show how to build an api
flask-blueprint: this how to separete endpoits using blueprints
flask-cache: this app show how to use the default config for redis
flask-celery: app with defined tasks to add paralelization with celery library
flask-logging: using logging library to add and get logs
flask-login-decorator: app axample to demostrate how to use decorator for login
flask-migrate: app example to demonstrate the migrations steps using alembic
flask-pymongo: app exmple to demostrate how to connectioon in mongo db using flask
flask-redis: app that show the use of redis in a simple way
flask-rest-sqlite: a simple rest app builded using sqlite
flask-session: controling sessions
flask-sqlite: database for sqlite
flask-test: test example using unittest and pytest

Details
------------

All those applications should be dockerized and in some case use docker compose to compose the needed dependencies


Installation
------------

You can create a virtual environment and install the required packages with the following commands:

    $ virtualenv venv
    $ . venv/bin/activate
    (venv) $ pip install -r requirements.txt

Running on Docker
--------------------

Since we have enabled each project folder with Docker, we cab up each service with the containers.

For running all:

    $ docker up

For running a specific:

    $ docker up flask-login


Running the Examples
--------------------

With the virtual environment activated you can `cd` into any of the examples and run the main script.

For examples 1-6:

    (venv) $ python hello.py

For example 7:

    (venv) $ python manage.py


Repositories
--------------------

flask-api
flask-blueprint
flask-cache
flask-celery
flask-logging
flask-login-decorator
flask-migrate
flask-pymongo
flask-redis
flask-rest-sqlite
flask-session
flask-sqlite
flask-test
