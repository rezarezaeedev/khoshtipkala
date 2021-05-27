from django.contrib import admin
from .models import *

class ContactUsAdmin(admin.ModelAdmin):
    list_display = [ 'userobject','__str__','fullname', 'email', 'is_read', 'active'    ]
    list_display_links = ['userobject','__str__','fullname', 'email']
    list_editable = [ 'is_read' ]
    list_filter = [ 'is_read', 'active']
    search_fields = ['userobject','subject','fullname', 'email']

    class Meta:
        model = ContactUs

admin.site.register(ContactUs,ContactUsAdmin)