# Generated by Django 3.2 on 2022-10-08 12:06

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220927_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(null=True, upload_to=accounts.models.upload_img),
        ),
    ]
