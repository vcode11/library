# Generated by Django 2.2.6 on 2019-10-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Loan'), ('a', 'Available'), ('r', 'Reserved'), ('d', 'Due')], default='a', help_text='Book Availability', max_length=1),
        ),
    ]
