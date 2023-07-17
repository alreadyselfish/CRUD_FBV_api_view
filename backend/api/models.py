from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)

