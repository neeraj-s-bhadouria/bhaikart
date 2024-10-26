from django.shortcuts import render
from .models.product import Product
from .models.category import Category


# index page where we will show all the products
def index(request):
    category_id = request.GET.get('category')
    products = Product.get_products_by_category_id(category_id) if category_id else Product.get_all_products()
    categories = Category.get_all_categories()
    return render(request, 'index.html', {'products': products, 'categories': categories})
# Create your views here.
