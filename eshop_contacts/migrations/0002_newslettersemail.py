# Generated by Django 3.1.7 on 2021-06-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewslettersEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='حذف شده/موجود')),
                ('active', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
            ],
            options={
                'verbose_name': 'ایمیل',
                'verbose_name_plural': 'ایمیل های خبرنامه',
            },
        ),
    ]
