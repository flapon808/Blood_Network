from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from bloodbank import views



urlpatterns = [
    path("bloodbank",views.Bloodbank,name="bloodbank"),
    path("donate",views.donate,name="donate"),
    path("donate.html",views.donate,name="donate"),
   
]
