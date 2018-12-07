from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from content.models import Book
from utils import rank
from utils import check, qread
from celery_task.tasks import qbuy

def show(request, book_id):

    rank.add_rank_for_week(book_id)

    book = Book.objects.get(pk=book_id)

    rank_books = rank.get_rank_for_week(5) # 查询前5的阅读排行

    return render(request, 'book/show.html', locals())


def free_read(request, book_id):
    # 获取当前登录用户的id
    user_id = check.get_login_user_id(request)
    if user_id is None:
        return JsonResponse({'code':100, 'msg':'未登录'})

    # 判断当前的抢读的时间段，以及已抢购的栈中是否最大
    qbuy.delay(user_id, book_id)
    return JsonResponse({'code':201, 'msg':'正在抢'})


def query_read_state(request, book_id):
    user_id = check.get_login_user_id(request)
    if user_id is None:
        return JsonResponse({'code': 100, 'msg': '未登录'})

    code, msg = qread.check_q_read_state(user_id, book_id)

    return JsonResponse({'code': code, 'msg': msg})
