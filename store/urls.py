from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup', views.register),
    path('login', views.login),
]