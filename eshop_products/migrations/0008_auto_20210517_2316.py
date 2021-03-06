# Generated by Django 3.1.7 on 2021-05-17 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=10, validators=[django.core.validators.MinValueValidator(10, 'کمترین قیمت 10 هزار تومان میباشد')], verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large'), ('XXL', 'XX-Large'), ('XXXL', 'XXX-Large')], default='M', max_length=4, verbose_name='سایز لباس'),
        ),
    ]
