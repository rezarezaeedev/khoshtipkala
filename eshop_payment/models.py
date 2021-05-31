from django.db import models

class PaymentGateway(models.Model):
    title=models.CharField(max_length=50,verbose_name='نام شرکت پرداخت')
    gatewaySite=models.URLField(verbose_name='آدرس سایت پرداخت')
    clientURL=models.URLField(verbose_name='لینک درگاه پرداخت (Client)',)
    startPayURL=models.URLField(verbose_name='آدرس شروع پرداخت (Start pay)',)
    merchantID=models.CharField(max_length=100,default='none',verbose_name='کد درگاه پرداخت (Merchant-ID)')
    callBackUrl=models.CharField(max_length=50,default='payment/verify/1',verbose_name='لینک بازگشت (CallbackURL)')
    server=models.CharField(max_length=50,default='localhost:8000/',verbose_name='آدرس سرور (Server)')
    gatewayLogoScript=models.TextField(verbose_name='اسکریپت اعتماد')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name='درگاه پرداخت'
        verbose_name_plural='درگاه های پرداخت'

    def __str__(self):
        return self.title