# Generated by Django 2.2.6 on 2019-10-17 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191018_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='initialized',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_shelf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Shelf'),
        ),
    ]