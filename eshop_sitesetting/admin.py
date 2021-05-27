from django.contrib import admin

from eshop_sitesetting.models import SiteSetting

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'titleEnglish', 'owner','mobile','tel','address','__aboutus__', ]
    list_display_links =  ['title', 'titleEnglish', 'owner','mobile','tel','address'  ]
    list_filter = ['active']
    search_fields = ['title', 'titleEnglish', 'owner','mobile','tel','address','aboutus']

admin.site.register(SiteSetting,SiteSettingAdmin)