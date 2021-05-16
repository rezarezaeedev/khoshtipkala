from django.db import models
import os
import time

def upload_image_path(instance, filepath):
    name, ext=get_name_extention(filepath)
    Time=f'{time.gmtime().tm_hour}:{time.gmtime().tm_min}:{time.gmtime().tm_sec}'
    base_directory='products'
    final_name=f'{instance.id}-{Time}-{instance.title}{ext}'
    final_path_and_name=os.path.join(base_directory, final_name)
    return final_path_and_name

def get_name_extention(filepath):
    basename    =   os.path.basename(filepath)
    name, ext   =   os.path.splitext(basename)
    return name, ext

class Product(models.Model):
    class clothzSize(models.TextChoices):
        Small = 'S', ('Small')
        Medium = 'M', ('Medium')
        Large = 'L', ('Large')
        XLarge = 'XL', ('X-Large')
        XXLarge = 'XXL', ('XX-Large')
        XXXLarge = 'XXXL', ('XXX-Large')

    title       =   models.CharField(max_length=120)
    desc        =   models.TextField()
    size        =   models.CharField(choices=clothzSize.choices,blank=False,null=False,max_length=4)
    price       =   models.DecimalField(decimal_places=2,max_digits=100)
    image       =   models.ImageField(upload_to=upload_image_path)
    active      =   models.BooleanField(default=True)

    class Meta:
        verbose_name='کالا'
        verbose_name_plural='محصولات'

    def __str__(self):
        return self.title
