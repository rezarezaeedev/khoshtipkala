from django.urls import path
from .views import *
urlpatterns=[
    path('login',login_user, name='login'),
    path('register',register_user, name='register'),
    path('logout',logout_user, name='logout'),
    path('user',user_account_main, name='user'),
    path('user/edit',edit_profile_user, name='edit'),
    path('user/support',support, name='support'),
]