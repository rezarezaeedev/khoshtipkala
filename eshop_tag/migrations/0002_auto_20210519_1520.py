# Generated by Django 3.1.7 on 2021-05-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_tag', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='titlePersian',
        ),
        migrations.AddField(
            model_name='tag',
            name='titleEnglish',
            field=models.CharField(default='s', max_length=20, verbose_name='عنوان انگلیسی'),
            preserve_default=False,
        ),
    ]
