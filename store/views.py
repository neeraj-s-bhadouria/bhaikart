from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.user import User


# index page where we will show all the products
def index(request):
    category_id = request.GET.get('category')
    products = Product.get_products_by_category_id(category_id) if category_id else Product.get_all_products()
    categories = Category.get_all_categories()
    return render(request, 'index.html', {'products': products, 'categories': categories})


# method to render the sign-up page
def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        error_msg = None
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        pwd = request.POST.get('pwd')

        if(not fname or not lname or not phoneNo or not pwd or not email or not phoneNo):
            error_msg = 'All fields are required.'
        elif(len(fname) < 2 or len(fname) > 20):
            error_msg = 'First name should be between 2 and 20 characters long.'
        elif(len(lname) < 2 or len(lname) > 20):
            error_msg = 'Last name should be between 2 and 20 characters long.'
        elif(len(phoneNo) > 14 or len(phoneNo) < 10 or not phoneNo.isdigit()):
            error_msg = 'Invalid phone number. It should be max of 14 digits long with country code.'
        elif(len(pwd) < 4 or len(pwd) > 25):
            error_msg = 'Password should be between 4 and 25 characters long.'
        else:
            user = User(first_name=fname, last_name=lname,
                        email=email, contact_no=phoneNo,
                        password=pwd)
            user.save()
            print('Registration Successful')
            return render(request, 'index.html', {'msg' : 'Registration Successful'})

        return render(request, 'signup.html', {'error_msg' : error_msg})

