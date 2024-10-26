from django.contrib import admin
from .models.product import Product
from .models.category import Category

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)

admin.site.register(Product, AdminProduct)
admin.site.register(Category)
