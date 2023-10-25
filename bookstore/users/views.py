from django.shortcuts import render, HttpResponseRedirect

from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm

from django.contrib import auth

from django.contrib.auth.decorators import login_required

from books.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('books:index'))
    else:
        form = UserLoginForm()
    context = {'form': form, 'title': 'Авторизация'}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form, 'title': 'Регистрация'}
    return render(request, 'users/registration.html', context)


@login_required(login_url='users:login')
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user,
                               files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    basket = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in basket)
    total_quantity = sum(basket.quantity for basket in basket)
    context = {'title': 'Личный кабинет', 'form': form, 'basket': basket,
               'total_sum': total_sum, 'total_quantity': total_quantity}
    return render(request, 'users/profile.html', context)
