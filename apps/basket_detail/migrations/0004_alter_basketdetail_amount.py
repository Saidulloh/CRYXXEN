# Generated by Django 4.1.3 on 2022-12-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_detail', '0003_remove_basketdetail_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketdetail',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='amount'),
        ),
    ]
