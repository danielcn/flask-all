FROM python:3.8.3-slim-stretch

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python", "run.py"]
