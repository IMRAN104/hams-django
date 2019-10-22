from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='familys'),
    path('create/', views.create, name='create-family'),
    # path('edit/', views.home),
]
