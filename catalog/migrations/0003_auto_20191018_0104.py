# Generated by Django 2.2.6 on 2019-10-17 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_shelf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of shelf', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_copies',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='book_shelf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Shelf'),
        ),
    ]