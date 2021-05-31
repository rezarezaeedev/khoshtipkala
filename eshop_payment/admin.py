from django.contrib import admin

# Register your models here.
from eshop_payment.models import PaymentGateway

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ['title','callBackUrl','server','active']
    list_display_links = ['title','callBackUrl','server']
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['title','callBackUrl','server','active']

admin.site.register(PaymentGateway,PaymentGatewayAdmin  )
