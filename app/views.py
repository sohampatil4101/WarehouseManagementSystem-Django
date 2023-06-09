from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime
from datetime import date
import time
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    context = {'username': request.session.get('username'), 'so': Warehouse.objects.all()}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')


def register(request):
    
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']

        if ( len(username) and len(email) and len(password1) and len(pincode)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (Register.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif ( Register.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}


        else:                       
            ins = Register(username = username, email = email, password = password1, state = state, city =city, pincode = pincode)
            ins.save()

            try:
                mssg = "You have successfully registered at Warehouse management... your username is " + username + "Thankyou!!!"
                send_mail(
                'Congratulations!!!',
                mssg,
                'settings.EMAIL_HOST_USER',
                [email], #here it can be also a list of emails
                fail_silently = False)

            except:
                pass

            context = {'success': True, 'mssg': "Registered successfully!!!"}
            return render(request, 'register.html', context)


    return render(request, 'register.html', context)


def login(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)
        request.session['username'] = username

        if (Register.objects.filter(username=username, password = password).exists()):
            # login(request, user)
            so = Register.objects.filter(username = username)
            context = {'username': request.session.get('username'), 'so': so}
            return redirect("/",context)



        else:
            context= {'success':True, 'mssg':"Please enter correct username or password!!!"}
            return render(request, 'login.html', context)



    return render(request, 'login.html', context)


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')


def addwarehouse(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        warehousename = request.POST['warehousename']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        lenght = request.POST.get('lenght')
        bredth = request.POST.get('bredth')
        height = request.POST.get('height')
        images = request.FILES.get('images')
        area = (int(lenght)*int(bredth)*int(height))
        date = datetime.today()
        
        if (Warehouse.objects.filter(warehousename = warehousename, username = username).exists()):
            context={'success': True, 'mssg':" Warehouse name exist"}
            return render(request, 'addwarehouse.html', context)

        else:
            ins = Warehouse(username = username,warehousename = warehousename,state = state,city = city,pincode = pincode,lenght = lenght,bredth = bredth,height = height,images = images,area = area,date = date)
            ins.save()

            return render(request, 'addwarehouse.html', context)



    return render(request, 'addwarehouse.html')


def deletewarehouse(request, obj1, obj2):
    abc = Warehouse.objects.get(username = obj1, warehousename = obj2)
    abc.delete()
    return redirect("/")


def viewhouse(request, obj1, obj2):
    context = {'so': Good.objects.filter(username = obj1, warehousename = obj2), 'warehousename': obj2}
    return render(request, 'viewhouse.html', context)


def deleteproduct(request, obj1, obj2, obj3):
    abc = Good.objects.get(username = obj1, warehousename = obj2, goodname = obj3)
    abc.delete()
    context = {'so': Good.objects.filter(username = obj1, warehousename = obj2), 'warehousename': obj2}
    return render(request, 'viewhouse.html', context)

def addproduct(request, obj1):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        abc = obj1
        username = request.session.get('username')
        warehousename = obj1
        goodname = request.POST.get('goodname')
        lenght = request.POST.get('lenght')
        bredth = request.POST.get('bredth')
        height = request.POST.get('height')
        images = request.FILES.get('images')
        area = (int(lenght)*int(bredth)*int(height))
        date = datetime.today()
        
        if (Good.objects.filter(warehousename = warehousename, goodname = goodname).exists()):
            context={'success': True, 'mssg':" Product exist", 'warehousename': obj1}
            return render(request, 'addproduct.html', context)

        else:
            ins = Good(abc = abc, username = username,warehousename = warehousename,goodname = goodname,lenght = lenght,bredth = bredth,height = height,images = images,area = area,date = date)
            ins.save()
            context={ 'warehousename': obj1}


            return render(request, 'addproduct.html', context)


    context={ 'warehousename': obj1}
    return render(request, 'addproduct.html', context)

def expiredproduct(request, obj1):
    so = Good.objects.filter(username = request.session.get('username'), warehousename = obj1 )
    context = {'warehousename': obj1, 'so': so, 'date': date.today()}
    return render(request, 'expiredproduct.html', context)



def search(request, obj1):
    context = {'success': False, 'warehousename': obj1}
    
    if request.method == "GET":
        context = {'success': False}
        search = request.GET['search']
        so = Good.objects.filter(username = request.session.get('username'), warehousename = obj1,  goodname__icontains = search)    
        if(so):
            context = {'so': so, 'warehousename': obj1, 'success': False} 
            return render(request, 'search.html', context)
        else:
            context = {'success': True, 'warehousename': obj1} 
            return render(request, 'search.html', context)

    else:
        context = {'success': True, 'warehousename': obj1}
        return render(request, 'search.html', context)
        
    return render(request, 'search.html', context)