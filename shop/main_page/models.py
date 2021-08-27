from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.TextField(max_length=30)
    model = models.TextField(max_length=30)
    year = models.TextField(max_length=30)
    vin = models.TextField(max_length=30)
    price_currency = models.TextField(max_length=3)
    price = models.DecimalField(max_digits=11, decimal_places=2,)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
