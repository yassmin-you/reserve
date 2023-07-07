from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import info
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'pages/home.html')

def reservation(request):
     
    submitted = False

    if request.method == 'POST':
        name=request.POST['name']
        whatsapp=request.POST['whatsapp']
        number=request.POST['number']
        academic_year=request.POST['academic']
        
        new_info=info(name=name,whatsapp=whatsapp,parent_number=number,academic_year=academic_year)
        new_info.save()
        return HttpResponseRedirect('/reservation?submitted=True')

    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/reservation.html', {'submitted': submitted})


def signin(request):

    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user= authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'مدخلات خاطئة')
            return redirect('signin')

    return render(request,'pages/login.html')

def signout(request):
    logout(request)
    messages.error(request,'تم تسجيل الخروج بنجاح')
    return redirect('home') 