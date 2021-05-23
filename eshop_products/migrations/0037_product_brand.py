# Generated by Django 3.1.7 on 2021-05-23 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_brands', '0001_initial'),
        ('eshop_products', '0036_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='eshop_brands.brand', verbose_name='برند محصول'),
            preserve_default=False,
        ),
    ]
