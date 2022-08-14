from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#
# # Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password = request.POST['psw']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid credential")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['Username']
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['email']
        password = request.POST['psw']
        cpassword = request.POST['psw-repeat']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return  redirect('register')
            else:
                user =User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                print("user created",user)
                return redirect('login')
        else:
            messages.info(request, "password mismatching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
