from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.user import User
from django.contrib.auth.hashers import make_password, check_password


# index page where we will show all the products
def index(request):
    category_id = request.GET.get('category')
    products = Product.get_products_by_category_id(category_id) if category_id else Product.get_all_products()
    categories = Category.get_all_categories()
    return render(request, 'index.html', {'products': products, 'categories': categories})

# method to handle validations for signup form
def validate_register_input(fname, lname, email, phoneNo, pwd, checkbox):
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

# method to proceed registration if no error is there else throw an error and return to the signup page
def do_registration(fname, lname, email, phoneNo, pwd, error_msg, request):
    if not error_msg:
        user = User(first_name=fname, last_name=lname,
                    email=email, contact_no='+' + phoneNo,
                    password=make_password(pwd))
        user.save()
        print('Registration Successful')
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

# method to render the sign-up page
def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        pwd = request.POST.get('pwd')
        error_msg = validate_register_input(fname, lname, email, phoneNo, pwd, request.POST.get('checkbox'))
        return do_registration(fname, lname, email, phoneNo, pwd, error_msg, request)

# method to log in the user
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        user = User.objects.get(email=email)
        if user and check_password(pwd, user.password):
            print('Login Successful - ', email)
            return redirect('homepage')
        else:
            data = {'error_msg': 'Invalid email or password.'}
            return render(request, 'login.html', data)
