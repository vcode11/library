#-*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('login/', views.userlogin, name="login"),
    path('', views.index, name="index"),
    path('log_out/', views.userlogout, name="userlogout"),
    path('sign_up/', views.usersignup, name="signup"),    
]