"""foodieblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include, re_path
=======
from django.urls import path, include
>>>>>>> 9e524bd088ed0f18ac4b93ae4d8045055fa4c7bd
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('index.urls')),
<<<<<<< HEAD
    path('account/',include('account.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) 
=======
    path('login/',include('login.urls')),
    path('admin/', admin.site.urls),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
# urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) 
>>>>>>> 9e524bd088ed0f18ac4b93ae4d8045055fa4c7bd
