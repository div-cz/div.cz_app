# Generated by Django 4.2.4 on 2023-11-10 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0044_alter_userprofile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='ratings',
        ),
    ]
