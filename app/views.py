import json
import os
import codecs

from markdown import markdown
import sys
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.conf import settings
from os import path
from datetime import datetime

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


def pages(request, page_name='index'):
    page_path = '{}/pages/{}.md'.format(path.dirname(__file__), page_name)
    page_path_html = '{}/pages/{}.html'.format(path.dirname(__file__), page_name)

    status = 200
    base_file = 'base_md.html'

    if path.exists(page_path):
        input_file = codecs.open(page_path, mode="r", encoding="utf-8").read()
        text = markdown(input_file)
    else:
        if not path.exists(page_path_html):
            return handler404(request, None)

        base_file = path.basename(page_path_html)
        text = ''

    return render(request, base_file, {
        'title': page_name.replace('_', ' ').replace('-', ' ').title(),
        'content': text,
        'pagename': page_name,
        'current_date': datetime.now()
    }, status=status)


def handler404(request, exception):
    return pages(request, page_name='404')


def logged_in(request):
    return 'user_info' in request.session and request.session['user_info'] != ''
