from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','gender', 'size',  'price', 'active']
    list_per_page = 10
    list_filter = ['gender', 'size', 'active']
    search_fields = ['title',]
    class Meta:
        model = Product

class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'product' ,'image']

    class Meta:
        model = ProductGallery


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductGallery,ProductGalleryAdmin)
