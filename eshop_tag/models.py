from django.db import models
# from eshop_products.models import Product
from django.db.models.signals import pre_save, post_save
from .utils import *

class Tag(models.Model):
    titlePersian     =   models.CharField(max_length=20,verbose_name='عنوان')
    titleEnglish  =   models.CharField(max_length=20,verbose_name='عنوان انگلیسی')
    slug      =   models.SlugField(unique=True, verbose_name='عنوان در url')
    timestamp =   models.DateTimeField(auto_now_add=True)
    active    =   models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    # products  =   models.ManyToManyField(Product, blank=True, verbose_name='محصولات مشمول')

    def __str__(self):
        return self.titlePersian

    class Meta:
        verbose_name            =   'برچسب'
        verbose_name_plural     =   'برچسب ها'

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    slug=instance.slug
    if slug is not None:
        slug=unique_slug_generator(instance, 6)

pre_save.connect(tag_pre_save_receiver, sender=Tag)
