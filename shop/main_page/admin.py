from django.contrib import admin
from .models import Car, Newsletter, MailMessage, Client
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

admin.site.register(Car)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_added',)
    models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols': 10})}
    models.CharField: {'widget': TextInput(attrs={'size': '20'})}


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(MailMessage)
admin.site.register(Client)
