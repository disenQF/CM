from utils import rd


def add_q_read(user_id, book_id):
    if rd.hexists('qbuy', user_id):
        return 202, '已抢过'

    elif rd.hlen('qbuy') < 15:
        rd.hset('qbuy', user_id, book_id)
        return 200, '抢成功'


def check_q_read_state(user_id, book_id):
    # key = qbuy  - hash
    # 判断当前用户是否存在 qbuy中
    if rd.hexists('qbuy', user_id):
        buy_book_id = rd.hget('qbuy', user_id).decode()
        if book_id == buy_book_id:
            return 200, '抢成功'  # 抢成功
        else:
            return 202, '已抢过'

    elif rd.hlen('qbuy') < 15:  # 栈的最大值 100 本书
        return 201, '正在抢'

    return 300, '已抢完'
