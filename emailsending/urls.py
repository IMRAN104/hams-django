from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_email_serve_page, name='send_email_serve_page')

]
