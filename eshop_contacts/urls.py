from django.urls import path
from .views import *

urlpatterns = [
    path('contact-us', contact_us, name='contact-us'),

]
