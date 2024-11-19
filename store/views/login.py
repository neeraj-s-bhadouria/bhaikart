from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View
from store.models import User


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(email=email).first()
        if user and check_password(pwd, user.password):
            print('Login Successful - ', email)
            request.session['userEmail'] = user.email
            request.session['userId'] = user.id
            return redirect('homepage')
        else:
            data = {'error_msg': 'Invalid email or password.'}
            return render(request, 'login.html', data)