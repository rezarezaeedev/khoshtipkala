from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','gender', 'size',  'price', 'active']
    list_per_page = 10
    search_fields = ['title',]
    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)
