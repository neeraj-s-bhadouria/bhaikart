from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Foreign key relationship with Category model.
    description = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category_id=category_id)
        else:
            return Product.get_all_products()