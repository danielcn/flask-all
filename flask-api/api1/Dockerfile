FROM python:3.8.5-slim-buster

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install

EXPOSE 5001

CMD ["pipenv", "run", "python", "app.py"]
