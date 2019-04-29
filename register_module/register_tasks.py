import time
import random
from celery import Celery

app = Celery('register_tasks_celery', backend='rpc://', broker='amqp://guest:guest@localhost:5672//')

def insert_db(userId):
    time.sleep(random.random() / 10)

@app.task
def send_email(email):
    time.sleep(random.random())

@app.task
def send_welcome(userId):
    time.sleep(random.random())