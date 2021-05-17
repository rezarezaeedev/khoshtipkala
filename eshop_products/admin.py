from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'size', 'price', 'active']
    list_per_page = 4

    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)