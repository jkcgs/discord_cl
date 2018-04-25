from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^oauth/login$', views.oauth_login, name='oauth_login'),
    url(r'^oauth/return$', views.oauth_return, name='oauth_return'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^(?P<page_name>[\w\-_]+)$', views.pages, name='pages'),
    url(r'^pages/(?P<page_name>[\w\-_]+)$', views.pages_redirect, name='pages'),
]
