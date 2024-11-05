from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from store.models import User


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        pwd = request.POST.get('pwd')
        error_msg = self.validate_register_input(fname, lname, email, phoneNo, pwd, request.POST.get('checkbox'))
        return self.do_registration(fname, lname, email, phoneNo, pwd, error_msg, request)


    # method to proceed registration if no error is there else throw an error and return to the signup page
    def do_registration(self, fname, lname, email, phoneNo, pwd, error_msg, request):
        if not error_msg:
            user = User(first_name=fname, last_name=lname,
                        email=email, contact_no='+' + phoneNo,
                        password=make_password(pwd))
            user.save()
            print('Registration Successful')
            request.session['user'] = user.email
            return redirect('homepage')
        else:
            data = {
                'error_msg': error_msg,
                'values': {
                    'fname': fname,
                    'lname': lname,
                    'email': email,
                    'phoneNo': phoneNo,
                }
            }
            return render(request, 'signup.html', data)


    # method to handle validations for signup form
    def validate_register_input(self, fname, lname, email, phoneNo, pwd, checkbox):
        error_msg = None
        if (not fname or not lname or not phoneNo or not pwd or not email or not phoneNo):
            error_msg = 'All fields are required.'
        elif (len(fname) < 2 or len(fname) > 20):
            error_msg = 'First name should be between 2 and 20 characters long.'
        elif (len(lname) < 2 or len(lname) > 20):
            error_msg = 'Last name should be between 2 and 20 characters long.'
        elif (len(phoneNo) > 14 or len(phoneNo) < 10 or not phoneNo.isdigit()):
            error_msg = 'Invalid phone number. It should be max of 14 digits long with country code.'
        elif (len(pwd) < 4 or len(pwd) > 25):
            error_msg = 'Password should be between 4 and 25 characters long.'
        elif (not checkbox):
            error_msg = 'Please agree to the terms and conditions.'
        return error_msg