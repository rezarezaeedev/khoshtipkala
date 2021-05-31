from django.urls import path
from .views import *

urlpatterns = [
    path('add-user-order',add_user_order,name='add-user-order'),
    path('user-open_order',user_open_order_list,name='user-open_order'),
    path('user-open_order/change-count/<objid>/<mode>', change_count_product_in_open_order, name='change_count_product_in_open_order'),
]