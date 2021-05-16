from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model
from .forms import *
from django.contrib.auth.models import User # or: User=get_user_model()

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    loginform=loginForm(request.POST or None)
    context={
        'loginform':loginform,
    }
    if loginform.is_valid():
        username=loginform.cleaned_data.get('username')
        password=loginform.cleaned_data.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not  None:
            login(request, user,backend=None)
            context['wl']=1
            return redirect('/')
        else:
            loginform.add_error('password','رمز عبور اشتباه است!!')
    return render(request,'account/login.html',context)

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    registerform = registerForm(request.POST or None)
    context = {
        'registerform':registerform,
    }
    if registerform.is_valid():
        username=registerform.cleaned_data.get('username')
        password=registerform.cleaned_data.get('password')
        email=registerform.cleaned_data.get('email')
        newUser=User.objects.create_user(username=username, password=password, email=email)
        return redirect('/login')
    return render(request, 'account/register.html', context)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


