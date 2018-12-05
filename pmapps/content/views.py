from django.shortcuts import render

# Create your views here.
from content.models import Book
from utils import rank


def show(request, book_id):

    rank.add_rank_for_week(book_id)

    book = Book.objects.get(pk=book_id)

    rank_books = rank.get_rank_for_week(5) # 查询前5的阅读排行

    return render(request, 'book/show.html', locals())