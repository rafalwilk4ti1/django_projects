from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Car, Newsletter, MailMessage, Client
from phonenumber_field.formfields import PhoneNumberField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name', 'model', 'year', 'vin', 'price_currency', 'price', 'header_image')


class NewsletterUser(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('name', 'email')


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'


# Create a Client form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'email', 'phone_cell', 'model_car')







