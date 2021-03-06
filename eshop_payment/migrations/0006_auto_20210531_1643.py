# Generated by Django 3.1.7 on 2021-05-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_payment', '0005_auto_20210531_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentgateway',
            name='domain',
        ),
        migrations.AddField(
            model_name='paymentgateway',
            name='server',
            field=models.CharField(default='localhost:8000/', max_length=50, verbose_name='آدرس سرور'),
        ),
        migrations.AlterField(
            model_name='paymentgateway',
            name='clientURL',
            field=models.URLField(verbose_name='لینک درگاه پرداخت(Client)'),
        ),
        migrations.AlterField(
            model_name='paymentgateway',
            name='startPayURL',
            field=models.URLField(verbose_name='آدرس شروع پرداخت(Start pay)'),
        ),
    ]
