from content.models import Book
from utils import rd


def add_rank_for_week(book_id):
    # 判断key是否存在
    existed = rd.exists('week_rank')

    rd.zincrby('week_rank', book_id)  # amount=1
    if not existed:
        rd.expire('week_rank', 604800)  # 一周的有效时间


def get_rank_for_week(top_n):
    '''
    返回周排行的前 top_n 个小说
    @:param top_n 前几本小说的排行
    :return: [( <Book>,  reads), ....]
    '''
    rank_ids = rd.zrevrange('week_rank', 0, top_n - 1, withscores=True)

    return [(Book.objects.get(pk=id_.decode()), round(score)) for id_, score in rank_ids]
