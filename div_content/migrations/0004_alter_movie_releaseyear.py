# Generated by Django 4.2.4 on 2023-09-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0003_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='releaseyear',
            field=models.CharField(max_length=4),
        ),
    ]
