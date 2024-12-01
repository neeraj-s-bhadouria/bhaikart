from django import template

register = template.Library()

@register.filter(name='total_price_for_product')
def get_total_price(product_price, product_quantity):
    return product_price * product_quantity

@register.filter(name='get_status_by_status_id')
def get_status_by_status_id(status_id):
    if status_id == 1:
        return 'Pending'
    elif status_id == 2:
        return 'Shipped'
    elif status_id == 3:
        return 'Out for Delivery'
    elif status_id == 4:
        return 'Delivered'
    elif status_id == 5:
        return 'Cancelled'
    elif status_id == 6:
        return 'Returned'
    elif status_id == 7:
        return 'Returned - Refunded'
    elif status_id == 8:
        return 'Completed'
    else:
        return 'Unknown'