from django.core import validators
from django.db import models
import os
import time
from django.db.models.signals import pre_save
from .utils import *

def get_name_extention(filepath):
    basename    =   os.path.basename(filepath)
    name, ext   =   os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filepath):
    name, ext=get_name_extention(filepath)
    Time=f'{time.gmtime().tm_hour}-{time.gmtime().tm_min}-{time.gmtime().tm_sec}'
    base_directory='products'
    final_name=f'{Time}-{instance.title}{ext}'
    final_path_and_name=os.path.join(base_directory, final_name)
    return final_path_and_name

class ProductManager(models.Manager):
    def get_active_products(self,active=True):
        objects=self.get_queryset().filter(active=active)
        return objects

class Product(models.Model):
    class clothzSize(models.TextChoices):
        Small = 'S', ('Small')
        Medium = 'M', ('Medium')
        Large = 'L', ('Large')
        XLarge = 'XL', ('X-Large')
        XXLarge = 'XXL', ('XX-Large')
        XXXLarge = 'XXXL', ('XXX-Large')

    objects=ProductManager()
    objid       =   models.CharField(max_length=10,editable=False)
    title       =   models.CharField(max_length=120, verbose_name='عنوان')
    desc        =   models.TextField( verbose_name='توضیحات')
    size        =   models.CharField(choices=clothzSize.choices,default=clothzSize.Medium,blank=False,null=False,max_length=4, verbose_name='سایز لباس')
    price       =   models.DecimalField(decimal_places=0, max_digits=10, validators=[validators.MinValueValidator(10, 'کمترین قیمت 10 هزار تومان میباشد')], verbose_name='قیمت', default=100)
    image       =   models.ImageField(upload_to=upload_image_path, verbose_name='تصویر')
    # slug        =   models.SlugField(unique=True,verbose_name='اسلاگ')
    active      =   models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name='کالا'
        verbose_name_plural='محصولات'

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.objid=='':
        newObjid = get_unique_string_id(instance, 5)
        instance.objid=newObjid

pre_save.connect(product_pre_save_receiver, sender=Product, )




