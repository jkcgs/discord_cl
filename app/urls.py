from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pages/(?P<page_name>[\w\-_]+)$', views.pages, name='pages'),
    url(r'^oauth/login$', views.oauth_login, name='oauth_login'),
    url(r'^oauth/return$', views.oauth_return, name='oauth_return'),
    url(r'^user$', views.user, name='user'),
    url(r'^logout$', views.logout, name='logout')
]
