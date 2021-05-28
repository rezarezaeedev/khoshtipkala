# Generated by Django 3.1.7 on 2021-05-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0046_favoriteproducts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoriteproducts',
            options={'verbose_name': 'محصول مورد علاقه', 'verbose_name_plural': 'لیست علاقمندی ها'},
        ),
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]