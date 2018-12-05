from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^show/(\d+)/', views.show),
]
