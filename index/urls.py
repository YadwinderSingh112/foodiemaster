from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    # path("authorpost/", views.AuthorView, name= "authorview"),
    path("article_detail/<str:slug>", views.category_single.as_view(), name="article_detail"),
#path("article_detail/<str:slug>/comment/", views.comments, name="commentView"),
    path("like/<str:slug>", views.likeView, name="likeView"),
    path("add_post/", views.Add_PostView, name= "add_post"),
    path("category_grid/", views.category_grid, name="category_grid"), 
    path("category_grid/<str:categ>", views.category_grid, name="category_grid"),
    path("category_list/", views.category_list, name="category_list"),
    path("category_list/<str:categ>", views.category_list, name="category_list"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    #path("edit/<str:slug>", views.UpdatePost.as_view(), name="update_post"),
]