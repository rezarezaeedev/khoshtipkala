from django.shortcuts import render

def header(request, *args, **kwargs):
    contect={
        'data':'در ایام کرونا با خرید آنلاین از شیوع بیشتر این بیماری جلوگیری کنید',
    }
    return render(request, 'shared/Header.html', contect)

def footer(request, *args, **kwargs):
    context={
        'about_us':'تمامی حقوق این وب سایت متعلق به رضا رضایی میباشد',
    }
    return render(request, 'shared/Footer.html', context)

def home(request):
    context={
        'data':'new data',
    }
    return render(request, 'homepage.html', context)