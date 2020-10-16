FROM python:3.8-slim-stretch

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python", "app.py"]
