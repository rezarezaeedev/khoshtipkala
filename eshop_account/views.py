import itertools

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model

from eshop_contacts.forms import ContactForm
from eshop_contacts.models import ContactUs
from .forms import *
from django.contrib.auth.models import User # or: User=get_user_model()

# get grouped list ,for gallery or recomended products
def list_grouper(n, iterable):
    args = [iter(iterable)] * n
    return list(([e for e in t if e != None] for t in itertools.zip_longest(*args)))

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

@login_required(login_url='/login')
def user_account_main(request):
    user=request.user

    context = {
        'point':0,
        'user':user
    }
    if 1:
        if user.username != '':
            context['point'] += 20
        else:
            context['username'] = 1
        if user.email != '':
            context['point'] += 20
        else:
            context['email'] =1
        if user.first_name != '':
            context['point'] += 20
        else:
            context['first_name'] = 1
        if user.last_name != '':
            context['point'] += 20
        else:
            context['last_name'] = 1
        if 'phone' == '':
            context['point'] += 20
        else:
            context['phone'] = 1
        # # context['point'] = 100 # for test
    return render(request, 'account/account_profile.html', context)


@login_required(login_url='/login')
def edit_profile_user(request):
    user = request.user
    edituserdataform=EditUserDataForm(request.POST or None, initial={'username':user.username,'first_name':user.first_name,'last_name':user.last_name,'email':user.email })

    context = {
        'edituserdataform': edituserdataform,
        'submitstatus':0

    }

    if edituserdataform.is_valid():
        username = edituserdataform.cleaned_data.get('username')
        email    = edituserdataform.cleaned_data.get('email')
        if User.objects.filter(username=username).exclude(id=user.id).exists():
            context['submitstatus']=-1
        elif User.objects.filter(email=email).exclude(id=user.id).exists():
            context['submitstatus']=-2
        else:
            user.username = username
            user.first_name = edituserdataform.cleaned_data.get('first_name')
            user.last_name = edituserdataform.cleaned_data.get('last_name')
            user.email = email
            user.save()
            context['submitstatus']=1



    return render(request, 'account/edit_account_profile.html', context)


def panel_profile_partial(request):
    context = {

    }
    return render(request, 'components/account_panel_partial.html', context)

def support(request):
    user=request.user
    contactus=user.contactus_set.all().order_by('-id')

    context={
        'contactus': contactus
    }

    return render(request, 'account/support_and_comment.html', context=context)





