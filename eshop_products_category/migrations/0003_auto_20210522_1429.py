# Generated by Django 3.1.7 on 2021-05-22 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0002_auto_20210520_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='name',
            new_name='slug',
        ),
    ]
