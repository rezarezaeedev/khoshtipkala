# Generated by Django 3.1.7 on 2021-05-16 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_account', '0003_auto_20210516_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large'), ('XXL', 'XX-Large'), ('XXXL', 'XXX-Large')], max_length=4),
        ),
    ]
