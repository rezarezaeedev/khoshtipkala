import os
import time

from django.db import models
def get_name_extention(filepath):
    basename    =   os.path.basename(filepath)
    name, ext   =   os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filepath):
    name, ext=get_name_extention(filepath)
    Time=f'{time.gmtime().tm_hour}-{time.gmtime().tm_min}-{time.gmtime().tm_sec}'
    base_directory='Sellers'
    final_name=f'{Time}-{instance.shopName}{ext}'
    final_path_and_name=os.path.join(base_directory, final_name)
    return final_path_and_name

class Seller(models.Model):
    shopName  = models.CharField(max_length=50,verbose_name='نام فروشگاه')
    firstName = models.CharField(max_length=50,verbose_name='نام')
    lastName  = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    image     = models.ImageField(upload_to=upload_image_path ,verbose_name='پروفایل')
    bio       = models.TextField(max_length=400,verbose_name='درباره')
    address   = models.TextField(max_length=400,verbose_name='آدرس')
    mobile    = models.CharField(max_length=13,verbose_name='شماره موبایل')
    tel       = models.CharField(max_length=13,verbose_name='شماره تلفن',blank=True)
    instagram = models.CharField(verbose_name='آیدی اینستاگرام',default=r'https://instagram.com',max_length=50)
    telegram  = models.CharField(verbose_name='آیدی تلگرام',default=r'https://telegram.org',max_length=50)
    soroush   = models.CharField(verbose_name='آیدی سروش',default=r'https://hi.splus.ir',max_length=50)
    github    = models.CharField(verbose_name='آیدی گیتهاب',default=r'https://github.com',max_length=50)
    linkdin    = models.CharField(verbose_name='آیدی لینکدین',default=r'https://linkdin.com',max_length=50)
    active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشندگان'

    def __str__(self):
        return self.shopName