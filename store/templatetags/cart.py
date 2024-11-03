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