# Generated by Django 4.2.4 on 2023-12-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0054_alter_bookpublisher_publishername'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpublisher',
            name='publisherwww',
            field=models.CharField(blank=True, db_column='PublisherWWW', max_length=255, null=True),
        ),
    ]
