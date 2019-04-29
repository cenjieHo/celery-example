from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'select_populate_book':{
        'task': 'favorite_book_exp.favorite_book.select_populate_book',
        'schedule': timedelta(seconds=10)
    }
}