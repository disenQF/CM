from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from content import views
from content.content_views import BookSearchView

urlpatterns = [
    url(r'^show/(\d+)/', views.show),
    url(r'^q_read/(\d+)/', views.free_read),
    url(r'^search/$', BookSearchView()),
    url(r'^query_state/(\d+)/', views.query_read_state),
]
