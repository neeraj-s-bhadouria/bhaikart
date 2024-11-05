from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product_id, request):
    cart = request.session.get('cart')
    if cart:
        for id in cart.keys():
            if int(id) == product_id:
                data = {
                    'in_cart': True,
                    'quantity': cart[id]
                }
                return data
    data = {
        'in_cart': False,
        'quantity': 0
    }
    return data

@register.filter(name='total_price_for_product')
def total_price_for_product(product_price, product_quantity):
    return product_price * product_quantity