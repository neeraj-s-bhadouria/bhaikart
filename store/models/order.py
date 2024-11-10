from django.db import models
from store.models import Product
from store.models import User


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, default='')
    contact_no = models.CharField(max_length=14, default='')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'{self.customer.first_name} - {self.product.name}'