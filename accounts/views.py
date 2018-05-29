from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    #check if request is post
    if request.method == 'POST':
        #authenticate user details
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        #if username and password is not empty log in the user  and redirect to home page
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            #redirect the user to login page with the error
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect'})

    else:
        return render(request,'accounts/login.html')
def singup(request):
    if request.method == 'POST':
        #user wants to sing up
        #checking if passwords matches
        if request.POST['password1'] == request.POST['password2']:
            try:
                #is their a user with that username
                user = User.objects.get(username=request.POST['username'])
                #if user exists return singup page with "username has already been taken"
                return render(request,'accounts/singup.html',{'error':"username has already been taken"})

            except User.DoesNotExist:
                #if user does not exist then a new create user
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                #log in the user
                auth.login(request,user)
                #redirect the user to the homepage
                return redirect('home')
        else:
            return render(request,'accounts/singup.html',{'error':"Password did not match"})

    else:
        #user wants to enter info
        return render(request,'accounts/singup.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
        
