from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 1

    def get_queryset(self):
        objects = Product.objects.get_active_products()
        return objects

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['objects']=self.get_queryset()
        return context


def product_detail(request, *args, **kwargs): # or...(request, slug):
    objid=kwargs['objid']
    title=kwargs['title']
    try:
        product = Product.objects.get(objid=objid,title=title, active=True)
    except Product.DoesNotExist:
        return render(request, '404_error.html')
    except:
        return Http404('--Bad error')
    context = {
        'product':product,
    }
    return render(request, 'products/product_detail.html', context)
