# Generated by Django 4.1.3 on 2022-12-12 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_remove_product_owner'),
        ('favorite', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ManyToManyField(to='product.product'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
