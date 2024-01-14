# Generated by Django 4.2.4 on 2023-12-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0060_bookauthor_birth_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookauthor',
            name='birth_year',
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='birthyear',
            field=models.IntegerField(blank=True, db_column='BirthYear', null=True),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='deathyear',
            field=models.IntegerField(blank=True, db_column='DeathYear', null=True),
        ),
    ]
