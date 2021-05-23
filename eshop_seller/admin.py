from django.contrib import admin
from .models import *

class SellerAdmin(admin.ModelAdmin):
    list_display = ['shopName', 'firstName','lastName','mobile', 'address']

    class Meta:
        model = Seller

admin.site.register(Seller,SellerAdmin)