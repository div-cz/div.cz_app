# Generated by Django 4.2.4 on 2023-12-27 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0070_book_databazeknih_book_goodreads'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authorid',
            field=models.ForeignKey(db_column='BookAuthor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.bookauthor'),
        ),
    ]
