from django.contrib import admin
from .models import *

class SellerAdmin(admin.ModelAdmin):
    list_display = ['shopName', 'firstName','lastName','mobile', 'address','active']
    list_filter = ['active']
    list_editable = ['active']
    list_display_links = ['shopName', 'firstName','lastName','mobile', 'address']
    search_fields = ['shopName', 'firstName','lastName','mobile', 'address','bio','tel','instagram','telegram','soroush','linkdin','github' ]

    class Meta:
        model = Seller

admin.site.register(Seller,SellerAdmin)