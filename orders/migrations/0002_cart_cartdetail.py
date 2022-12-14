# Generated by Django 3.2 on 2022-11-10 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generatr_code


class Migration(migrations.Migration):

    dependencies = [
        ('proudct', '0007_auto_20221008_1406'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=utils.generatr_code.generate_code, max_length=8)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantiy', models.IntegerField(max_length=10)),
                ('price', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=80, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_detail', to='orders.cart')),
                ('proudct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proudct_cart', to='proudct.proudct')),
            ],
        ),
    ]
