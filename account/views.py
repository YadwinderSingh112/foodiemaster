# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import *

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        password = request.POST.get('Password')

        user = authenticate(username = user_name, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login_user')
    else:
        return render(request, 'login.html')

def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password')
        password2 = request.POST.get('Confirm Password')

        if password1 == password2:
            if CustomUser.objects.filter(username = user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')

            elif CustomUser.objects.filter(email = email).exists():
                messages.info(request, 'email taken')
                return redirect('signup')

            else:
                user = CustomUser.objects.create_user(username = user_name,password = password1, email = email, is_reader = True )
                user.save()
                print('User created')
                return redirect('login_user')
        else:
            messages.info(request, 'password is not a match')
            return redirect('signup')
    else:
        return render(request, 'login.html')

def Sign_out(request):
    logout(request)
    return redirect('login_user')

