def session_context(request):
    data = {}
    if request.session['logged']:
        data['user'] = {
            'name': request.session['user_info']['username'],
            'avatar': 'https://cdn.discordapp.com/avatars/{}/{}.png'.format(
                request.session['user_info']['id'], request.session['user_info']['avatar']
            )
        }

    return data
