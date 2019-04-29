from register_module.register_tasks import *

from flask import Flask
app = Flask(__name__)

@app.route('/register/<userId>/<email>')
def register(userId, email):
    # print('注册新账号："', userId, '"...')
    insert_db(userId)
    send_email(email)
    send_welcome(userId)
    # print('注册新账号："', userId, '"成功！')
    return 'success'

@app.route('/celery/register/<userId>/<email>')
def celery_register(userId, email):
    # print('注册新账号："', userId, '"...')
    insert_db(userId)
    send_email.delay(email)
    send_welcome.delay(userId)
    # print('注册新账号："', userId, '"成功！')
    return 'success'

if __name__ == '__main__':
    app.run()