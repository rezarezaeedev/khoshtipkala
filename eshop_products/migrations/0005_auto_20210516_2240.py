# Generated by Django 3.1.7 on 2021-05-16 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_auto_20210516_2219'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinLengthValidator(2, 'کمترین قیمت 10 هزار تومان میباشد')], verbose_name='قیمت'),
        ),
    ]