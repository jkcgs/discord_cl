from django.conf.urls import url
from django.urls import path

from app.views import pages, session, manage

urlpatterns = [
    path('', pages.index, name='index'),
    path('oauth/login', session.oauth_login, name='oauth_login'),
    path('oauth/return', session.oauth_return, name='oauth_return'),
    path('logout', session.log_out, name='logout'),
    path('pages/alexis', pages.alexis_redir),
    path('alexis', pages.alexis_redir),
    path('manage/pages', manage.pages, name='mgr_pages'),
    path('api/commands', manage.commands, name='commands'),
    url(r'^(?P<page_name>[\w\-_]+)$', pages.pages, name='pages'),
    url(r'^pages/(?P<page_name>[\w\-_]+)$', pages.pages_redirect, name='pages_redir'),
]
