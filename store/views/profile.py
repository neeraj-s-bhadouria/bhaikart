from django.shortcuts import render, redirect
from ..models.product import Product

def logout(request):
    user_email = request.session.get('user')
    print('Logout request for - ', user_email)
    request.session.clear()
    print('Session deleted successfully for - ', user_email)
    return redirect('login')

def show_cart(request):
    cart = request.session.get('cart')
    total_price = 0
    data = {
        'cart': cart,
        'total_price': total_price
    }
    if cart:
        products = Product.get_products_by_id(list(cart.keys()))
        print(products)
        for product in products:
            total_price += product.price * cart[str(product.id)]
        data['total_price'] = total_price
        data['products'] = products
    return render(request, 'cart.html', data)