from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("login_user", views.login_user, name="login_user"),
    path("signout", views.Sign_out, name="signout"),
    path("signup", views.sign_up, name="signup")
]