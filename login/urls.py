from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("signin", views.signin, name="signin"),
    #path("signout", views.Sign_out, name="signout"),
    # path("signup", views.sign_up, name="signup")
]