# Generated by Django 4.2.4 on 2023-10-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0014_moviecomments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.CharField(db_column='Popularity', db_index=True, max_length=6, null=True),
        ),
    ]
