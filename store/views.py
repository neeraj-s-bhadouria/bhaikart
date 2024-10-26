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
        user = User(first_name=request.POST.get('fname'), last_name=request.POST.get('lname'),
                    email=request.POST.get('email'), contact_no=request.POST.get('phoneNo'),
                    password=request.POST.get('pwd'))
        user.save()
        print('Registration Successful')
        return render(request, 'index.html')

