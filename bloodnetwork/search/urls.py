from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from search import views



urlpatterns = [
    path('search.html',views.search,name="Search1"),
    path('search',views.search,name="Search"),
    path('result',views.result,name="result"),
    path('result.html',views.result,name="result1"),
    path('showinfo/<str:pk>/', views.Showinfo, name='showinfo'),

]
# 