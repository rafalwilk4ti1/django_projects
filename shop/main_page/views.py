from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required # used to check if user is logged
from .forms import CreateUserForm, NewsletterUser, MailMessageForm, ClientForm
from .models import Car, Newsletter, Client
from django.core.mail import send_mail
from django_pandas.io import read_frame


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

@login_required(login_url='login')
def about(request):
    car = Car.objects.all()
    context = {'car': car}
    return render(request, 'main_page/about.html', context)


@login_required(login_url='login')
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful! :) ')
            return redirect('/newsletter')
    else:
        form = NewsletterUser()

    context = {
        'form': form,
    }

    return render(request, 'main_page/newsletter.html', context)

@login_required(login_url='login')
def mail_letter(request):
    emails = Newsletter.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent to the Main List! :)')
            return redirect('sendemails')

    else:
        form = MailMessageForm()

    context = {
        'form': form,
    }
    return render(request, 'main_page/send_emails.html', context)


def purchase(request):
    submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Excellent, we will send you our offer, and call you.')
            return HttpResponseRedirect('/purchase?submitted=True')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True

    form = ClientForm
    return render(request, 'main_page/purchase.html', {'form': form, 'submitted':submitted})


def catalog(request):
    car = Car.objects.all()

    car_paginator = Paginator(car, 10)

    page_num = request.GET.get('page')

    page = car_paginator.get_page(page_num)

    context = {
        'car': car_paginator.count,
        'page': page
    }

    return render(request, 'main_page/catalog.html', context)


@login_required(login_url='login')
def contact(request):
    car = Car.objects.all()
    clients = Client.objects.all()
    context = {'car': car,
               'client': clients}


    return render(request, 'main_page/contact.html', context)