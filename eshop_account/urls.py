from django.urls import path
from .views import *
urlpatterns=[
    path('login',login_user, name='login'),
    path('register',register_user, name='register'),
    path('logout',logout_user, name='logout'),
]