import itertools

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from eshop_order.forms import OrderForm
from .forms import CommentForm, FavoriteForm
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
        context = super().get_context_data()
        request = self.request
        context['products'] = self.get_queryset()
        return context


def register_comment(commentform, product, request):
    name = commentform.cleaned_data.get('name')
    email = commentform.cleaned_data.get('email')
    text = commentform.cleaned_data.get('text')
    rate = commentform.cleaned_data.get('rate')
    userobject = request.user
    CommentProduct.objects.create(name=name, email=email, text=text, product=product, userobject=userobject, rate=rate)


def add_product_to_favorite(product, request):
    owner = request.user
    if FavoriteProducts.objects.filter(product=product, owner=owner).count() == 0:
        FavoriteProducts.objects.create(owner=owner, product=product)
    else:
        FavoriteProducts.objects.filter(product=product, owner=owner).delete()


def product_detail(request, *args, **kwargs):  # or...(request, slug):
    objid = kwargs['objid']
    title = kwargs['title']
    commentform = CommentForm(request.POST or None)
    try:
        product = Product.objects.get(objid=objid, active=True)
        product.visit_count += 1
        product.save()
        product_gallery = ProductGallery.objects.filter(product_id=product.id)
        product_gallery = list_grouper(3, product_gallery)
        recomended_products_lookup = (Q(brand=product.brand) |
                                      Q(categories__in=product.categories.all()) |
                                      Q(tags__in=product.tags.all())
                                      )
        recomended_products = Product.objects.filter(recomended_products_lookup, active=True,
                                                     gender=product.gender).exclude(id=product.id).distinct()
        recomended_products = list_grouper(3, recomended_products)
        comments = CommentProduct.objects.filter(product_id=product.id)

    except Product.DoesNotExist:
        return redirect('/404-error')
    except:
        return redirect('/404-error')

    orderdetailform = OrderForm(request.POST or None, initial={'product_objid': objid})
    favoriteform = FavoriteForm(request.POST or None, initial={'product_objid': objid})
    if not request.user.is_anonymous:
        favoriteproduct = FavoriteProducts.objects.filter(product=product, owner=request.user).exists()
    else:
        favoriteproduct = 0

    context = {
        'product': product,
        "product_gallery": product_gallery,
        "comments": comments,
        "commentform": commentform,
        "recomended_products": recomended_products,
        "orderdetailform": orderdetailform,
        "favoriteform": favoriteform,
        "favoriteproduct": favoriteproduct,

    }

    if favoriteform.is_valid():
        add_product_to_favorite(product, request)
        context['favoriteform'] = FavoriteForm()
        return redirect(
            reverse('productdetail', kwargs={'objid': product.objid, 'title': product.title.replace(' ', '-')}))

    if commentform.is_valid():
        register_comment(commentform, product, request)
        commentform = CommentForm()
        context['commentform'] = commentform
        return redirect(reverse('productdetail', args=[product.objid, product.title.replace(' ', '-')]))

    return render(request, 'products/product_detail.html', context)


class SearchProductList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        request = self.request
        context['products'] = self.get_queryset()
        context['searchFlag'] = True
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('query')

        if query is not None:
            lookup = (Q(title__icontains=query) |
                      Q(desc__icontains=query) |
                      Q(tags__titlePersian__icontains=query)
                      )
            products = Product.objects.filter(lookup, active=True)
            products = products.distinct()  # remove duplicate items
            if products.count() != 0:
                return products
        return Product.objects.filter(objid=' ')


class CategoryList_partial(ListView):
    template_name = 'components/product_category_partial.html'

    def get_queryset(self):
        return ProductCategory.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        request = self.request
        context['products'] = self.get_queryset()
        return context


class ProductsBycategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category = self.kwargs['category']
        products = Product.objects.filter(categories__slug__iexact=category)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = self.kwargs['category']
        context['products'] = Product.objects.filter(categories__slug__iexact=category)
        return context


class BrandList_partial(ListView):
    template_name = 'components/product_brand_component.html'

    def get_queryset(self):
        return Brand.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['brands'] = Brand.objects.all()
        return context


class ProductByBrand(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        brand = self.kwargs['brand']
        objects = Product.objects.filter(brand__slug__iexact=brand, active=True)
        return objects

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        request = self.request
        context['products'] = self.get_queryset()
        return context


class FavoriteProductList(ListView):
    template_name = 'products/favorite_product_list.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        # favoritelist=FavoriteProducts.objects.filter(owner=user)
        favoritelist = user.favoriteproducts_set.all()
        products = list(map(lambda x: x.product, favoritelist))
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        request = self.request
        context['products'] = self.get_queryset()
        return context
