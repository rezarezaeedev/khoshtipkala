"""rezarezaeeshp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('', include('eshop_order.urls')),
    path('', include('eshop_account.urls')),
    path('', include('eshop_products.urls')),
    path('', include('eshop_contacts.urls')),
    path('404-error', not_fount_404_error, name='404-error'),
    path('payment/', include('eshop_payment.urls',namespace='payment')),
    path('latest-product-partial', latest_product_partial, name='latest-product-partial'),
    path('most_visited_product_partial', most_visited_product_partial, name='most-visited-product-partial'),
    path('category-home-product-partial', category_home_product_partial, name='category-home-product-partial'),
    path('about', about, name='about'),
    path('header', header, name='header'),
    # path('footer', footer, name='footer'),
    path('admin/', admin.site.urls),
]

handler404 = 'rezarezaeeshp.views.not_fount_404_error'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #add static files path to urls
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #add static media's path to urls
