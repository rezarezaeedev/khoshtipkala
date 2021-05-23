from django.contrib import admin
from eshop_brands.models import Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ['title','country']

    class Meta:
        model=Brand

admin.site.register(Brand,BrandAdmin)
