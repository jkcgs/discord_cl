def session_context(request):
    data = {}
    if 'logged' in request.session and request.session['logged']:
        data['dsuser'] = request.session['user_info']['username']
        data['avatar'] = 'https://cdn.discordapp.com/avatars/{}/{}.png'.format(
            request.session['user_info']['id'], request.session['user_info']['avatar']
        )

    return data
