from django.shortcuts import render,redirect
from User.models import Blood, District
from .models import bloodbank,Category,Donor
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Bloodbank(request):
    allbank=bloodbank.objects.all()
    allcatagory=Category.objects.all()
    context={
         "allbank":allbank,
         "allcatagory":allcatagory,
    }
    return render(request,"bloodbank/bloodbank.html",context)

@login_required(login_url='login')
def donate(request):
    return render(request,"donate/donate.html")


@login_required(login_url='login')
def donate(request):
    Bloodall=Blood.objects.all()
    dist=District.objects.all()
    bank=bloodbank.objects.all()
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dist=request.POST['district']
        area=request.POST['area']
        postal=request.POST['postalcode']
        date=request.POST['date']
        Blood1=request.POST['blood']
        b_bank=request.POST['bbank']

        
        ins = Donor(Donor_Name=name,Donor_Email=email,Donor_Phone=phone,Donor_District=dist,Donor_Area=area,Donor_Postalcode=postal,Date_Of_Donation=date,Donor_Bloodhroup=Blood1,Blood_Bank_Name=b_bank)
        ins.save()
        messages.success(request,'We Recived Your Information,THANK YOU')
        return redirect('/donate.html')



    
       

        return render(request,"donate/donate.html")
    context = {
        "dist": dist , 
        "Bloodall":Bloodall,
        "bank":bank,
     }
    #return HttpResponse("this is contact page (/contact)")
    return render(request,"donate/donate.html",context)
    