# Generated by Django 2.2.6 on 2019-10-19 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20191019_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='number_of_copies',
        ),
    ]