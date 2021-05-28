from django.contrib.auth.models import User
from django.db import models
from eshop_products.models import Product

class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    is_paid=models.BooleanField(default=False,verbose_name='پرداخت شده/نشده')
    payment_date=models.DateTimeField(blank=True,null=True,verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبد های خرید کاربران'

    def __str__(self):
        return  self.owner.get_full_name()

class OrderDetail(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='سبد خرید')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    price=models.IntegerField(verbose_name='قیمت محصول')
    count=models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name='جزئیات محصول'
        verbose_name_plural='اطلاعات جزئیات محصول'

    def __str__(self):
        return self.product.title

    def get_total_price(self):
        return self.count * self.price



