import itertools
from django.http import Http404,HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import CommentForm
from .models import *
from django.db.models import Q
from django.urls import reverse

def list_grouper(n, iterable):
    args = [iter(iterable)] * n
    return list(([e for e in t if e != None] for t in itertools.zip_longest(*args)))

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        objects = Product.objects.get_active_products()
        return objects

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        request=self.request
        context['products']=self.get_queryset()
        return context

def register_comment():
    pass

def product_detail(request, *args, **kwargs): # or...(request, slug):
    objid=kwargs['objid']
    title=kwargs['title']
    loggedIn=request.user.is_authenticated
    commentform = CommentForm(request.POST or None)
    try:
        product = Product.objects.get(objid=objid, active=True)
        product_gallery=ProductGallery.objects.filter(product_id=product.id)
        product_gallery=list_grouper(3,product_gallery)
        comments=CommentProduct.objects.filter(product_id=product.id)
    except Product.DoesNotExist:
        return render(request, '404_error.html')
    except:
        return Http404('--Bad error')

    context = {
        'product':product,
        "product_gallery":product_gallery,
        "comments":comments,
        "commentform":commentform,
        # 'statusComment':False,
        # 'loggedIn':loggedIn,
    }

    if commentform.is_valid():
            name = commentform.cleaned_data.get('name')
            email = commentform.cleaned_data.get('email')
            text = commentform.cleaned_data.get('text')
            CommentProduct.objects.create(name=name, email=email, text=text,product=product)
            commentform = CommentForm()
            context['commentform']= commentform
            return redirect(reverse('productdetail',kwargs={'objid':objid,'title':title}))


    return render(request, 'products/product_detail.html', context)

class SearchProductList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        request=self.request
        context['products']=self.get_queryset()
        context['searchFlag']=True
        return context

    def get_queryset(self):
        request=self.request
        query=request.GET.get('query')

        if query is not None:
            lookup=(Q(title__icontains=query) |
                    Q(desc__icontains=query) |
                    Q(tags__titlePersian__icontains=query)
                    )
            products=Product.objects.filter(lookup, active=True)
            products=products.distinct() # remove duplicate items
            if products.count() !=0:
                return products
        return Product.objects.filter(objid=' ')


class CategoryList_partial(ListView):
    template_name = 'components/product_category_partial.html'

    def get_queryset(self):
        return ProductCategory.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        request=self.request
        context['products']=self.get_queryset()
        return context


class ProductsBycategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category=self.kwargs['category']
        products = Product.objects.filter(categories__slug__iexact=category)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        category = self.kwargs['category']
        context['products']=Product.objects.filter(categories__slug__iexact=category)
        return context


class BrandList_partial(ListView):
    template_name = 'components/product_brand_component.html'

    def get_queryset(self):
        return Brand.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['brands']=Brand.objects.all()
        return context


class ProductByBrand(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        brand=self.kwargs['brand']
        objects = Product.objects.filter(brand__slug__iexact=brand,active=True)
        return objects

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        request=self.request
        context['products']=self.get_queryset()
        return context

