# Generated by Django 3.2 on 2022-09-16 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proudct', '0002_proudct_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='proudct',
            name='img',
            field=models.ImageField(default='', upload_to='ProudctImge', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proudct',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='proudct.brand', verbose_name='Brand'),
        ),
    ]