# Generated by Django 3.1.7 on 2021-05-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_payment', '0002_auto_20210531_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentgateway',
            name='title',
            field=models.CharField(max_length=50, verbose_name='نام شرکت پرداخت'),
        ),
    ]
