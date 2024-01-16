"""
URL configuration for a codestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views. Home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'), name='blog')
"""
import os
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This will include all url paths contained in urls.py under blog directory
    path('about/', include('about.urls'), name='about-urls'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog-urls'),
    path('__reload__/', include('django_browser_reload.urls'))
]
