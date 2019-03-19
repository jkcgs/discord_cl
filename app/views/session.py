import json
import os
import sys

from django.contrib.auth import login, logout
from django.http import HttpResponseBadRequest, HttpResponseForbidden

from django.shortcuts import redirect
from django.conf import settings

from oauthlib.oauth2 import InvalidGrantError
from requests_oauthlib import OAuth2Session

from app.models import DiscordAdmin

api_base = 'https://discordapp.com/api/v6'
client_id = settings.DISCORD_CLIENT_ID
client_secret = settings.DISCORD_CLIENT_SECRET
redirect_uri = settings.DISCORD_REDIRECT_URI
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope='email identify')


def oauth_login(request):
    if client_id == '' or client_secret == '' or redirect_uri == '':
        raise RuntimeError('Discord not properly set up, check DISCORD_* variables at settings.py')

    if logged_in(request):
        return redirect('/')

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

    if 'oauth_state' not in request.session or state != request.session['oauth_state']:
        return HttpResponseForbidden()

    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    try:
        oauth.fetch_token(api_base + '/oauth2/token', code=code, client_secret=client_secret)
    except InvalidGrantError:
        return redirect('/?error=invalid_grant')

    r = oauth.get(api_base + '/users/@me')
    data = json.loads(r.text)

    try:
        adm = DiscordAdmin.objects.get(userid=data['id'])
        request.session['user_info'] = data
        request.session['logged'] = True
        request.session['username'] = data['username']
        request.session['avatar'] = avatar_url(data)

        adm.nick = data['username']
        adm.save()

        if adm.dj_user is not None:
            login(request, adm.dj_user)

        return redirect('/')
    except DiscordAdmin.DoesNotExist:
        return redirect('/?error=not_authorized')


def log_out(request):
    if 'user_info' in request.session:
        del request.session['user_info']

    if 'logged' in request.session:
        del request.session['logged']

    if request.user.is_authenticated:
        logout(request)

    return redirect('/')


def logged_in(request):
    return 'user_info' in request.session and request.session['user_info'] != ''


def avatar_url(user):
    if user['avatar']:
        return 'https://cdn.discordapp.com/avatars/{uid}/{hash}.{ext}'.format(
            uid=user['id'], hash=user['avatar'],
            ext='gif' if user['id'].startswith('a_') else 'jpg'
        )
    else:
        return 'embed/avatars/{discriminator_mod}.png'.format(
            discriminator_mod=str(int(user['discriminator']) % 5)
        )
