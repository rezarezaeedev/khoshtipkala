# Generated by Django 3.1.7 on 2021-05-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sliders', '0006_auto_20210523_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='titleWhite',
            field=models.CharField(blank=True, max_length=70, verbose_name='عنوان دوم'),
        ),
    ]
