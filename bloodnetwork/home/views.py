from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url='login')
def home(request):
    return render(request,"home/home.html")

@login_required(login_url='login')
def aboutus(request):
    return render(request,"About_us.html")
