from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=14)
    password = models.CharField(max_length=500, blank=False)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + " " + self.last_name

