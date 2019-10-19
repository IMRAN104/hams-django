from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('details/<int:blog_id>/', views.blog_details, name='blog_details'),
    # path('details/<int: blog_id>/', views.blog_details, name='blog_details'),  If you give space after int: , it will throw an error in the url. So, you must avoid space inside that <>
]
