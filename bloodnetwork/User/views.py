from django.shortcuts import redirect, render
from User.models import profile
from django.contrib import messages
from .models import profile
from django.contrib.auth.decorators import login_required
from .forms import  Donorinfo


# Create your views here.
def editinfo(request):
    profile=request.user.profile
    forms = Donorinfo(instance=profile)
    if request.method=="POST":
         form =Donorinfo(request.POST,instance=profile)
         if form.is_valid():
              form.save()
              return redirect("profile.html")
    context = { 'forms' : forms}
    return render(request,'editinfo/editinfo.html', context)



def userProfile(request):
    profile=request.user.profile
    context={
         "profile":profile
    }
    return render(request,"profile/profile.html",context)