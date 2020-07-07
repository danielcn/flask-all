from celery import celery
from time import sleep

app  = Celery('tasks', 
  broker=app.config['CELERY_BROKER_URL'],
  backend=app.config['CELERY_RESULT_BACKEND'],
)

@app.task
def user_registered(user):
  sleep(5)
  return user