# Generated by Django 3.1.7 on 2021-05-16 17:49

from django.db import migrations, models
import django.db.models.manager
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0003_auto_20210516_1721'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=eshop_products.models.upload_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(max_length=12, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large'), ('XXL', 'XX-Large'), ('XXXL', 'XXX-Large')], max_length=4, verbose_name='سایز لباس'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
    ]
