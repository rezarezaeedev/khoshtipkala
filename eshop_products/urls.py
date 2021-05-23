from django.urls import path
from eshop_products.views import *

urlpatterns=[
    path('products', ProductsList.as_view(), name='products'),
    path('products/search', SearchProductList.as_view(), name='searchproducts'),
    path('CategoryList_partial', CategoryList_partial.as_view(), name='CategoryList_partial'),
    path('BrandList_partial', BrandList_partial.as_view(), name='BrandList_partial'),
    path('products/barnd/<brand>', ProductByBrand.as_view()),
    path('products/category/<category>', ProductsBycategory.as_view()),
    path('products/<objid>/<title>', product_detail, name='productdetail'),

]