# Generated by Django 4.2.4 on 2024-01-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0083_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, db_column='Pages', null=True),
        ),
    ]
