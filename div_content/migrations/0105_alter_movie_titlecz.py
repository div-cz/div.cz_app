# Generated by Django 4.2.4 on 2024-04-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0104_remove_tvshow_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='titlecz',
            field=models.CharField(db_column='TitleCZ', db_index=True, default='', max_length=255),
        ),
    ]