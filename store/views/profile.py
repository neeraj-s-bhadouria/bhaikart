from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.order import Order
from ..models.user import User
from store.middleware.auth import auth_middleware

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

# method to proceed with the checkout
@auth_middleware
def check_out(request):
    print(request.POST)
    customer = User.get_user_by_id(request.session.get('userId'))
    print('customer - ', customer)
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    print('address:', address, 'phone:', phone, 'customer:', customer)
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    print('products = ', products, ', cart = ', cart)
    for product in products:
        order = Order(product = product, customer = customer, address = address, contact_no = phone, quantity = cart.get(str(product.id)), price = product.price)
        order.save()
    request.session['cart'] = []
    return redirect('homepage')


# method to show order history
@auth_middleware
def order(request):
    userId = request.session.get('userId')
    orders = Order.fetch_order_history(userId)
    return render(request, 'orders.html', {'orders': orders})