from django.urls import path
from eshop_products.views import *

urlpatterns=[
    path('products', ProductsList.as_view(), name='products'),
    path('products/search', SearchProductList.as_view(), name='searchproducts'),
    path('products/<objid>/<title>', product_detail, name='productdetail'),

]