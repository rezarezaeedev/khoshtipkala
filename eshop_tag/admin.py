from django.contrib import admin
from .models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ['titlePersian', 'titleEnglish', 'slug', 'timestamp', 'active']
    class Meta:
        model=Tag

admin.site.register(Tag, TagAdmin)