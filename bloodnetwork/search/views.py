from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from User.models import profile, District, division,Blood
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')      
def search(request):
    allgroup=Blood.objects.all()
    alldivision=division.objects.all()
    if 'blood' in request.GET:
    #post=profile.objects.all()
        blood=request.GET['blood']
        area=request.GET['area']
        data =profile.objects.filter(Blood_Group=blood).filter(Area=area)
        return render(request,"result/result.html",{'data':data})
    else:
        data = profile.objects.all()
    context={
        'data': data ,'alldivision':alldivision,'allgroup':allgroup
            }
    return render(request,"search/search.html",context)
    

@login_required(login_url='login')    
def result(request):
    
    return render(request,"result/result.html")

@login_required(login_url='login')
def Showinfo(request,pk):
    detail = profile.objects.get(id=pk)
    context = {
        'details' : detail
    }
    return render(request, 'showinfo/showinfo.html', context)
