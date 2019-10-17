# Generated by Django 2.2.6 on 2019-10-17 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20191018_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'verbose_name': 'List of All Copies', 'verbose_name_plural': 'Book Copies'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, help_text='Add a author', related_name='books', to='catalog.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_shelf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.Shelf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Choose a genre for this book.', related_name='books', to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Loan'), ('a', 'Available'), ('r', 'Reserved'), ('l', 'Lost')], default='a', help_text='Book Availability', max_length=1),
        ),
    ]
