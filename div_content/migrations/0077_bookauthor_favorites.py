# Generated by Django 4.2.4 on 2023-12-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0076_book_pseudonym'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookauthor',
            name='favorites',
            field=models.IntegerField(blank=True, db_column='Favorites', null=True),
        ),
    ]
