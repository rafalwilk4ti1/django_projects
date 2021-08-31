from django.contrib import admin
from .models import Car, Newsletter, MailMessage, Client
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.


admin.site.register(MailMessage)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_added',)
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    ordering = ('name', 'email')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'vin', 'price')
    list_filter = ('name', 'year', 'price')
    search_fields = ('name', 'model')
    ordering = ('name', 'price')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone_cell', 'model_car')
    list_filter = ('surname', 'model_car')
    search_fields = ('surname', 'model_car')
    ordering = ('name', 'surname', 'email', 'model_car')

