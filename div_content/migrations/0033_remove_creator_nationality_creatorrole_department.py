# Generated by Django 4.2.4 on 2023-09-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0032_remove_creator_nationality_creatorrole_rolenamecz'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorrole',
            name='department',
            field=models.CharField(blank=True, db_column='Department', max_length=255),
        ),
    ]