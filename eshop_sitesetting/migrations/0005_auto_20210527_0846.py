# Generated by Django 3.1.7 on 2021-05-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sitesetting', '0004_auto_20210526_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='copyright',
            field=models.CharField(max_length=200, verbose_name='قانون کپی رایت'),
        ),
    ]
