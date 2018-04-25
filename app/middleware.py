class SessionInit:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'user_info' not in request.session:
            request.session['logged'] = False

        response = self.get_response(request)
        return response
