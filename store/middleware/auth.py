from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        print('middleware - ', request.session.get('userId'))
        if not request.session.get('userId'):
            return_url = request.META['PATH_INFO']
            return redirect(f'login?return={return_url}')  # Redirect to login page if user is not authenticated
        response = get_response(request)
        return response

    return middleware