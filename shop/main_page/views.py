from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required # used to check if user is logged
from .forms import CreateUserForm
from .models import Car

@login_required(login_url='login')
def main_page(request):
    car = Car.objects.all()
    context = {'car': car}
    return render(request, 'main_page/index.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'main_page/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.info(request, 'Username OR password is incorrect.')

        context = {}
        return render(request, 'main_page/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
