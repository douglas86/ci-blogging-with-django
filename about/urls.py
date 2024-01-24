from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutList.as_view(), name='about')
]
