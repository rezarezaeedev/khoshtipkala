# Generated by Django 3.1.7 on 2021-05-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_payment', '0004_paymentgateway_gatewaylogoscript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentgateway',
            name='callBackUrl',
            field=models.CharField(default='payment/verify/1', max_length=50, verbose_name='لینک بازگشت'),
        ),
    ]
