import os
import time

from django.contrib.auth.models import User
from django.db import models

def get_name_extention(filepath):
    basename    =   os.path.basename(filepath)
    name, ext   =   os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filepath):
    name, ext=get_name_extention(filepath)
    Time=f'{time.gmtime().tm_hour}-{time.gmtime().tm_min}-{time.gmtime().tm_sec}'
    base_directory=instance.__class__.__name__
    final_name=f'{Time}-{instance.title}{ext}'
    final_path_and_name=os.path.join(base_directory, final_name)
    return final_path_and_name

class SiteSetting(models.Model):
    title=models.CharField(max_length=150,verbose_name='عنوان سایت')
    titleEnglish=models.CharField(max_length=150,verbose_name='Title')
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='مالک سایت')
    address=models.TextField(max_length=500,verbose_name='آدرس')
    email=models.EmailField(max_length=150,verbose_name='ایمیل سایت')
    telegram=models.CharField(max_length=50,verbose_name='تلگرام',blank=True,null=True)
    instagram=models.CharField(max_length=50,verbose_name='اینستاگرام',blank=True,null=True)
    mobile=models.CharField(max_length=14,verbose_name='موبایل سایت')
    tel=models.CharField(max_length=14,verbose_name='تلفن سایت')
    fax=models.CharField(max_length=14,verbose_name='فکس سایت')
    aboutus=models.TextField(max_length=1000,verbose_name='درباره ما')
    copyright=models.CharField(max_length=200,verbose_name='قانون کپی رایت')
    image=models.ImageField(upload_to=upload_image_path,verbose_name='لوگو سایت (51*180)')
    mapurl=models.URLField(verbose_name='نشانی فروشگاه/دفتر')
    active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural='مدیریت تنظیمات'

    def __str__(self):
        return self.title

    def __aboutus__(self):
        return self.aboutus[:20]