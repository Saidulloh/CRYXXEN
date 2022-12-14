# Generated by Django 4.1.3 on 2022-12-11 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='You should write +996[code][number]', regex='^(\\+996)\\d{9}$')]),
        ),
    ]
