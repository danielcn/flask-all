FROM python:3.9.5-slim-stretch

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python", "run.py"]
