from django.shortcuts import render
from eshop_products_category.models import ProductCategory
from .utils import *
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

def most_visited_product_partial(request):
    products=Product.objects.filter(active=True).order_by('-visit_count')[:10]
    context={
        'products_grouped': list_grouper(4,products),
        'label': 'پر بازدید ترین محصولات'
    }
    return render(request, 'components/most_visit_product_partial.html', context)

def latest_product_partial(request):
    products=Product.objects.filter(active=True).order_by('-timestamp')[:10]
    context={
        'products_grouped': list_grouper(4,products),
        'label':'آخرین محصولات'
    }
    return render(request, 'components/latest_home_product_partial.html', context)

def category_home_product_partial(request):
    categories=ProductCategory.objects.all()
    grouped_products_categories=[]
    for category in categories[:8]:
        products_set=category.product_set.all().order_by('-id')[:4]
        if products_set.count() != 0:
            grouped_products_categories+=[products_set]
            continue
        categories=categories.exclude(id=category.id)

    context={
        'categories':categories,
        'grouped_products_categories':grouped_products_categories,

    }

    return render(request, 'components/category_home_product_partial.html',context)

def not_fount_404_error(request,*args, **kwargs): # (request, exception)
    sitesetting=SiteSetting.objects.filter(active=True).last()
    context = {
        'sitesetting':sitesetting,
    }

    return render(request, '404_error.html', context=context)






