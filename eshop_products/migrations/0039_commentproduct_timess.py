# Generated by Django 3.1.7 on 2021-05-23 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0038_commentproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentproduct',
            name='timess',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
