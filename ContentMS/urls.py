"""ContentMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

import xadmin as admin
from content.models import Category, Book

from utils import rank


def toIndex(request):
    # 从请求中获取cate_id参数
    cate_id = int(request.GET.get('cate_id', 0))

    # 所有一级分类
    cates = Category.objects.filter(parent__isnull=True).all()

    # 查询指定某一大类的小说
    if cate_id:
        books = Book.objects.filter(category__parent_id=cate_id)
    else:
        books = Book.objects.all()

    # 自定义分页 pages = count / pageSize.   offset = (page-1)*pageSize
    # sql :  select id,name from table limit offset, pageSize

    paginator = Paginator(books, 10)

    # 请求参数中的page,代表请求哪一页的数据
    page_num = int(request.GET.get('page', 1))
    pager = paginator.page(page_num)

    # 查询周排行榜
    rank_books = rank.get_rank_for_week(5)

    return render(request, 'index.html', locals())


def read_book(request, book_id):
    rank.add_rank_for_week(book_id)
    return redirect('/')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^book/', include('content.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^/', toIndex),  # 默认主页的请求路径
    url(r'', toIndex),  # 默认主页的请求路径

]
