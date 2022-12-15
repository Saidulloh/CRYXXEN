# Generated by Django 4.1.3 on 2022-12-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_owner'),
        ('basket', '0009_alter_basket_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(related_name='basket_products', to='product.product'),
        ),
    ]
