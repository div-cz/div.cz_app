# Generated by Django 4.2.4 on 2023-10-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0012_movie_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomments',
            name='commentid',
            field=models.AutoField(db_column='CommentID', primary_key=True, serialize=False, unique=True),
        ),
    ]
