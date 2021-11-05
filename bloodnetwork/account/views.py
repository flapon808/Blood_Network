from django import contrib
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import  DonorRegistration


# Create your views here.
def Registration(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
                forms.save()
                print(forms.errors)
                context_details ={
                    'forms' : forms
                }
                #After donor registation donor details display
                messages.success(request,'Succecfully Registerd')
                return render(request, 'login/login.html', context_details)
        else:
            messages.error(request,'Form INVALID')
    context = {
                'forms' : forms,
            }
    return render(request,'registration/registration.html', context)

    
def userlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/home.html")
        else:
             messages.error(request,'invalid Login') 
             return redirect('/login.html')
    else:
        return render(request,"login/login.html")

def userlogout(request):
    logout(request)
    return redirect('index')
   