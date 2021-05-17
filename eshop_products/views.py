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
    slug=kwargs['slug']
    title=kwargs['title']
    product = get_object_or_404(Product,slug=slug, active=True,title=title)
    context = {
        'product':product,
    }
    return render(request, 'products/product_detail.html', context)
