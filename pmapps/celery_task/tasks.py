from ContentMS.celery import capp
import time
from utils import qread


@capp.task
def qbuy(user_id, book_id):
    code, msg = qread.add_q_read(user_id, book_id)
    return 'code: %s, msg:\"%s\"' % (code, msg)