# Generated by Django 4.1.3 on 2022-12-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_remove_basket_product_basket_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='product',
            new_name='products',
        ),
    ]