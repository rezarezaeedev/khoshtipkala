# Generated by Django 3.1.7 on 2021-05-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_account', '0002_auto_20210516_0356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size2',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='w', max_length=2),
            preserve_default=False,
        ),
    ]
