from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Car(models.Model):
    name = models.TextField(max_length=30)
    model = models.TextField(max_length=30)
    year = models.TextField(max_length=30)
    vin = models.TextField(max_length=30)
    price_currency = models.TextField(max_length=3)
    price = models.DecimalField(max_digits=11, decimal_places=2,)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    amount_car = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return f'{self.name} {self.model}'


class Newsletter(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=40, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, null=True)
    phone_cell = PhoneNumberField(unique=True)
    model_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='model_car')
