# Generated by Django 4.1.3 on 2022-12-16 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='tite',
        ),
    ]
