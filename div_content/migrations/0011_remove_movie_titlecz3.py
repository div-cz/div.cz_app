# Generated by Django 4.2.4 on 2023-10-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0010_movie_titlecz3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='titlecz3',
        ),
    ]