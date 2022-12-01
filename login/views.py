from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def sign_in(request):
    return render(request, 'signin.html')

def sign_up(request):
    return render(request, 'signin.html')

def Sign_out(request):
    return redirect('signin.html')

def register(request):
    return render(request, 'regitser.html')
