# Generated by Django 4.2.4 on 2023-10-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0009_movierating_average_movierating_content_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='titlecz3',
            field=models.CharField(db_column='TitleCZ3', default='', max_length=255),
        ),
    ]
