import json
import os
import codecs

import markdown
import sys
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.conf import settings
from os import path

from oauthlib.oauth2 import InvalidGrantError
from requests_oauthlib import OAuth2Session

api_base = 'https://discordapp.com/api/v6'
client_id = settings.DISCORD_CLIENT_ID
client_secret = settings.DISCORD_CLIENT_SECRET
redirect_uri = settings.DISCORD_REDIRECT_URI
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope='email identify')


def index(request):
    return pages(request)


def oauth_login(request):
    if client_id == '' or client_secret == '' or redirect_uri == '':
        raise RuntimeError('Discord not properly set up, check DISCORD_* variables at settings.py')

    if logged_in(request):
        return redirect('/user')

    login_url, state = oauth.authorization_url(api_base + '/oauth2/authorize')
    request.session['oauth_state'] = state
    return redirect(login_url)


def oauth_return(request):
    if client_id == '' or client_secret == '' or redirect_uri == '':
        raise RuntimeError('Discord not properly set up, check DISCORD_* variables at settings.py')

    code = request.GET.get('code', '')
    state = request.GET.get('state', '')
    if code == '' or state == '':
        return HttpResponseBadRequest()

    if state != request.session['oauth_state']:
        return HttpResponseForbidden()

    if sys.argv[1] == 'runserver':
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    try:
        token = oauth.fetch_token(api_base + '/oauth2/token', code=code, client_secret=client_secret)
    except InvalidGrantError:
        return redirect('/?error=invalid_grant')

    r = oauth.get(api_base + '/users/@me')
    request.session['user_info'] = str(r.text)
    return redirect('/user')


def user(request):
    if not logged_in(request):
        return redirect('/?error=not_logged')

    info = request.session['user_info']
    print('raw_info: ' + info)
    return render(request, 'user.html', {
        'info': json.loads(info),
        'raw_info': info
    })


def logout(request):
    del request.session['user_info']
    return redirect('/')


def pages(request, page_name='index', webvars=None):
    page_path = '{}/pages/{}.md'.format(path.dirname(__file__), page_name)
    if not path.exists(page_path):
        return HttpResponseNotFound('<h1>Page not found</h1>')

    input_file = codecs.open(page_path, mode="r", encoding="utf-8")
    text = input_file.read()

    if webvars is None:
        webvars = {}

    return render(request, 'pages.html', {
        'title': page_name.replace('_', ' ').replace('-', ' ').title(),
        'content': markdown.markdown(text).format(**webvars)
    })


def logged_in(request):
    return 'user_info' in request.session and request.session['user_info'] != ''
