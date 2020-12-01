FROM python:3.8.6-slim-buster

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN  python -m pip install --upgrade pip

RUN pipenv install

CMD ["pipenv", "run", "python", "app.py"]
