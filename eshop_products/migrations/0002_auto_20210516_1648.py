# Generated by Django 3.1.7 on 2021-05-16 12:18

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'کالا', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(max_length=1),
        ),
    ]
