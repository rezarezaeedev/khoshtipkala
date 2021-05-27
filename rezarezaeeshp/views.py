from django.shortcuts import render

from eshop_sitesetting.models import SiteSetting
from eshop_sliders.models import *

def header(request, *args, **kwargs):
    sitesetting=SiteSetting.objects.all().last()
    context={
        'sitesetting':sitesetting
    }
    return render(request, 'shared/Header.html', context)

def footer(request, *args, **kwargs):
    sitesetting=SiteSetting.objects.all().last()
    context={
        'sitesetting':sitesetting
    }
    return render(request, 'shared/Footer.html', context)

def home(request):
    slider=Slide.objects.all()
    context={
        'slider':slider,
    }
    return render(request, 'homepage.html', context)

def about(request):
    sitesetting=SiteSetting.objects.all().last()
    context={
        'sitesetting':sitesetting
    }

    return render(request,'aboutpage.html',context)