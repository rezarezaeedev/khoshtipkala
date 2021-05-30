from django.urls import path

from .views import *

app_name='payment'
urlpatterns = [
    path(r'request', send_payment_request, name='send-payment-request'),
    path(r'verify/<order_id>',  verify_payment, name='verify-payment'),
]