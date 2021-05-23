from django.contrib import admin
from .models import *
# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)