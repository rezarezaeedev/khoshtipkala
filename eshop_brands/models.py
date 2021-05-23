from django.db import models

class Brand(models.Model):
    title       = models.CharField(max_length=120, verbose_name='عنوان')
    country     = models.CharField(max_length=20,verbose_name='کشور سازنده')
    slug        = models.SlugField(max_length=20,verbose_name='عنوان در url')

    class Meta:
        verbose_name='برند'
        verbose_name_plural='برند ها'

    def __str__(self):
        return self.title
