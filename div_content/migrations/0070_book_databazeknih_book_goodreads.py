# Generated by Django 4.2.4 on 2023-12-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0069_bookauthor_databazeknih_alter_bookauthor_goodreads'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='databazeknih',
            field=models.CharField(blank=True, db_column='DatabazeKnih', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='goodreads',
            field=models.CharField(blank=True, db_column='GoodreadsID', max_length=12, null=True),
        ),
    ]
