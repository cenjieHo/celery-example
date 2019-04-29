from celery import Celery
import time
app = Celery('notify_friends', backend='rpc://', broker='amqp://guest:guest@localhost:5672//')

@app.task
def notify_friends(userId, newsId):
    print('Start to notify_friends task at {0}, userId:{1} newsId:{2}'.format(time.ctime(), userId, newsId))
    time.sleep(2)
    print('Task notify_friends succeed at {0}'.format(time.ctime()))
    return True