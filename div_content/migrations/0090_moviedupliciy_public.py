# Generated by Django 4.2.4 on 2024-04-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0089_moviedupliciy'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedupliciy',
            name='public',
            field=models.IntegerField(db_column='Public', default=1),
        ),
    ]
