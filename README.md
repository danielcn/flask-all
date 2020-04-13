Flask-Intro
===========

Sample code from my "Introduction to Flask" presentation. The slides for this presentation are available at [https://speakerdeck.com/miguelgrinberg/introduction-to-flask](https://speakerdeck.com/miguelgrinberg/introduction-to-flask).


Repositories
------------
- Migrate

Requirements
------------

- flask-logging:
- flask-login-decorator:
- flask-migrate: app example to demonstrate the migrations steps using alembic
- flask-pymongo: app exmple to demostrate how to connectioon in mongo db using flask
- flask-redis: app that show the use of redis in a simple way
- flask-rest-sqlite: a simple rest app builded using sqlite
- flask-session: controling sessions
- flask-sqlite: database for sqlite


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

flask-logging
flask-login-decorator
flask-migrate
flask-pymongo
flask-redis
flask-rest-sqlite
flask-session
flask-sqlite
