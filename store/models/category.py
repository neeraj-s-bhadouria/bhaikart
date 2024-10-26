from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    @staticmethod
    def get_all_categories():
        return Category.objects.all()