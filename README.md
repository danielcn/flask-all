Flask-Examples
===========

Sample code from my "Introduction to Flask" presentation. 
The slides for this presentation are available at [https://speakerdeck.com/miguelgrinberg/introduction-to-flask](https://speakerdeck.com/miguelgrinberg/introduction-to-flask).


Repositories
------------
- Migrate

Repositories description
------------

- flask-api: show how to build an api
- flask-blueprint: this how to separete endpoits using blueprints
- flask-cache: this app show how to use the default config for redis
- flask-celery: app with defined tasks to add paralelization with celery library
- flask-feedback-app: general feedback app example
- flask-jwt: app to perfom authentitacion using jwt
- flask-k8s: app with the basic k8s implementation
- flask-logging: using logging library to add and get logs
- flask-login-decorator: app axample to demostrate how to use decorator for login
- flask-migrate: app example to demonstrate the migrations steps using alembic
- flask-postgree: app exaple using postgree database
- flask-probes: app to simulatef probes endpoints
- flask-pymongo: app exmple to demostrate how to connectioon in mongo db using flask
- flask-rabbitmq: connect to rabbitmq message queue mechanism
- flask-redis: app that show the use of redis in a simple way
- flask-rest-sqlite: a simple rest app builded using sqlite
- flask-sendmail: example of sendmail app
- flask-session: controling sessions
- flask-sqlite: database for sqlite
- flask-test: test example using unitiitest and pytest


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

Since we have enabled each project folder with Docker, we cab up some of those services using docker composer.

Running all registered:

    $ docker-composer up

Running a specific:

    $ cd flask-api
    $ docker-composer up flask-api


Running the Examples
--------------------

With the virtual environment activated you can `cd` into any of the examples and run the main script.

For examples 1-6:

    $ pipenv shell
    (venv) $ pipenv install
    (venv) $ python app.py

For example 7:

    (venv) $ python manage.py


Repositories
--------------------

[flask-api](https://github.com/danielcn/flask-all/tree/master/flask-api)

[flask-blueprint](https://github.com/danielcn/flask-all/tree/master/flask-blueprint)

[flask-cache](https://github.com/danielcn/flask-all/tree/master/flask-cache)

[flask-celery](https://github.com/danielcn/flask-all/tree/master/flask-celery)

[flask-feedback-app](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

[flask-jwt](https://github.com/danielcn/flask-all/tree/master/flask-jwt)

[flask-k8s](https://github.com/danielcn/flask-all/tree/master/flask-k8s)

[flask-logging](https://github.com/danielcn/flask-all/tree/master/flask-logging)

[flask-login-decorator](https://github.com/danielcn/flask-all/tree/master/flask-login-decorator)

[flask-migrate](https://github.com/danielcn/flask-all/tree/master/flask-migrate)

[flask-postgree](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

[flask-probes](https://github.com/danielcn/flask-all/tree/master/flask-probes)

[flask-pymongo](https://github.com/danielcn/flask-all/tree/master/flask-pymongo)

[flask-rabbitmq](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

[flask-redis](https://github.com/danielcn/flask-all/tree/master/flask-redis)

[flask-rest-sqlite](https://github.com/danielcn/flask-all/tree/master/flask-rest-sqlite)

[flask-sendmail](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

[flask-session](https://github.com/danielcn/flask-all/tree/master/flask-session)

[flask-sqlite](https://github.com/danielcn/flask-all/tree/master/flask-sqlite)

[flask-test](https://github.com/danielcn/flask-all/tree/master/flask-test)
