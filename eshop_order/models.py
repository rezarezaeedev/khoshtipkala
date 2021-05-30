from django.contrib.auth.models import User
from django.db import models
from eshop_products.models import Product
from eshop_sitesetting.models import SiteSetting


class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    is_paid=models.BooleanField(default=False,verbose_name='پرداخت شده/نشده')
    payment_date=models.DateTimeField(blank=True,null=True,verbose_name='تاریخ پرداخت')
    ref_id=models.CharField(max_length=100,blank=True,null=True, verbose_name='کد پیگیری پرداخت')
    # todo: user_owner_info=models.ForeignKey(SendInfo,on_delete=models.CASCADE,)

    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبد های خرید کاربران'

    def __str__(self):
        return  self.owner.get_full_name()

    # [0], |first: total price -[1], |last: total price seperated
    def get_total_price(self):
        amount=0
        orderdetails=self.orderdetail_set.all()
        for detail in orderdetails:
            amount+=detail.get_total_price()[0]
        amount_seperated=f'{amount:,}'
        return (amount, amount_seperated)


    # [0], |first: tax percent(9) -[1], |last: tax percent with precent sign(9%)
    def get_tax_percent(self):
        tax_percent = SiteSetting.objects.filter(active=True).last().tax_of_sell
        tax_percent_with_sign = f'{tax_percent}%'
        return (tax_percent, tax_percent_with_sign)


    # [0], |first: tax -[1], |last: tax seperated
    def get_tax_of_price(self):
        tax_percent=self.get_tax_percent()[0]
        tax=(self.get_total_price()[0] * tax_percent) /100
        tax_seperated=f'{tax:,}'
        return  (tax, tax_seperated)


    # [0], |first: total price with tax -[1], |last: total price with tax seperated
    def get_total_price_with_taxation(self):
        total_price=self.get_total_price()[0] + self.get_tax_of_price()[0]
        total_price_seperated=f'{total_price:,}'
        return  (total_price, total_price_seperated)


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

    # [0], |first: price -[1], |last: price seperated
    def get_price_seperated(self):
        price=self.price
        price_seperated=f'{price:,}'
        return price, price_seperated

    # [0], |first: total price -[1], |last: total price seperated
    def get_total_price(self):
        price=self.count * self.price
        price_seperated=f'{price:,}'
        return (price, price_seperated)











