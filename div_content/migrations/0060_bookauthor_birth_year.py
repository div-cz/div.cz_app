# Generated by Django 4.2.4 on 2023-12-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0059_bookauthor_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookauthor',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
