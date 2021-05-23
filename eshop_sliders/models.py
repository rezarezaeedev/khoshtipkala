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
    base_directory='sliders'
    final_name=f'{Time}-{instance.title}{ext}'
    final_path_and_name=os.path.join(base_directory, final_name)
    return final_path_and_name


class Slide(models.Model):
    title = models.CharField(max_length=70,verbose_name='عنوان')
    titleWhite = models.CharField(max_length=70,verbose_name='عنوان دوم',blank=True)
    desc  = models.TextField(max_length=250,verbose_name="توضیحات")
    link  = models.URLField(max_length=150,verbose_name='لینک')
    image = models.ImageField(upload_to=upload_image_path,verbose_name='تصویر')
    active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name='اسلایدر'
        verbose_name_plural='اسلایدر'

    def __str__(self):
        return self.title