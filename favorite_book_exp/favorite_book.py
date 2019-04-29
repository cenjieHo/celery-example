from celery import Celery
import time

app = Celery('select_populate_book', backend='rpc://', broker='amqp://guest:guest@localhost:5672//')
app.config_from_object('favorite_book_exp.config')

@app.task
def select_populate_book():
    print('Start to select_populate_book task at {0}'.format(time.ctime()))
    time.sleep(2)
    print('Task select_populate_book succeed at {0}'.format(time.ctime()))
    return True

