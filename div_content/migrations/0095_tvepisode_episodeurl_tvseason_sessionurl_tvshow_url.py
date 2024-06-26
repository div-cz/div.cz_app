# Generated by Django 4.2.4 on 2024-04-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0094_tvshow_universumid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvepisode',
            name='episodeurl',
            field=models.CharField(blank=True, db_column='EpisodeURL', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tvseason',
            name='sessionurl',
            field=models.CharField(blank=True, db_column='SessionURL', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='url',
            field=models.CharField(blank=True, db_column='URL', max_length=255, null=True),
        ),
    ]
