from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    # index page where we will show all the products
    def get(self, request):
        print('cart - ', request.session.get('cart'))
        print('user - ', request.session.get('userEmail'))
        category_id = request.GET.get('category')
        products = Product.get_products_by_category_id(category_id) if category_id else Product.get_all_products()
        categories = Category.get_all_categories()
        return render(request, 'index.html', {'products': products, 'categories': categories})

    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            cart[product_id] = cart.get(product_id) - 1 if remove else cart.get(
                product_id) + 1 if cart.get(product_id) else 1
            if cart.get(product_id) == 0:
                del cart[product_id]
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('homepage')
