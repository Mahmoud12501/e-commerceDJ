# Generated by Django 3.2 on 2022-11-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_cart_cartdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantiy',
            field=models.IntegerField(default=0),
        ),
    ]