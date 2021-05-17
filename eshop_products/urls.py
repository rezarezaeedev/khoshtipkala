from django.urls import path
from eshop_products.views import *

urlpatterns=[
    path('products', ProductsList.as_view(), name='products'),
    # path('products/<id>', product_detail, name='productdetail'),
    path('products/<objid>/<title>', product_detail, name='productdetail'),

]