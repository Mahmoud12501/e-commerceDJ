# Generated by Django 3.2 on 2022-09-26 14:21

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('proudct', '0005_alter_proudct_img'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='proudct',
            managers=[
                ('ad_manger', django.db.models.manager.Manager()),
            ],
        ),
    ]
