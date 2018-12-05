from django.conf.urls import url

from user import views
urlpatterns = [
    url(r'^regist/', views.regist),
    url(r'^regist_ajax/', views.regist_for_ajax),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^upload_img/', views.uploadImg),
]
