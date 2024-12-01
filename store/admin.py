from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.user import User
from .models.order import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)


class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_no')


class AdminOrder(admin.ModelAdmin):
    list_display = ('customer', 'product', 'price', 'quantity', 'date', 'status')


admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(User, AdminUser)
admin.site.register(Order, AdminOrder)