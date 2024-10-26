from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.user import User

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)


class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_no')


admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(User, AdminUser)
