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

class CommentProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'email' ,'rate', 'timestamp', 'active']
    list_display_links = ['__str__', 'name', 'email'  ,]
    list_editable = ['rate', 'active' ]
    search_fields = ['__str__', 'name', 'email' ]
    list_filter = ['rate', 'active']

    class Meta:
        model = CommentProduct

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductGallery,ProductGalleryAdmin)
admin.site.register(CommentProduct,CommentProductAdmin )
