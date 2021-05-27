from django.contrib.auth.models import User
from django.db import models

class ContactUs(models.Model):
    userobject=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='فرد کامنت گذارنده')
    fullname  =     models.CharField(max_length=50,verbose_name='نام و نام خانوادگی')
    email     =     models.EmailField(max_length=50,verbose_name='ایمیل')
    subject   =     models.CharField(max_length=200,verbose_name='موضوع')
    text      =     models.TextField(max_length=1000,verbose_name='متن پیام')
    is_read   =     models.BooleanField(default=False,verbose_name='خوانده شده/نشده')
    active   =     models.BooleanField(default=True,verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name='تماس باما'
        verbose_name_plural='پیام های کاربران'

    def __str__(self):
        return self.subject[:10]




















