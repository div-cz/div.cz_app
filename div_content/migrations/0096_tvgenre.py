# Generated by Django 4.2.4 on 2024-04-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0095_tvepisode_episodeurl_tvseason_sessionurl_tvshow_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tvgenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreid', models.ForeignKey(db_column='GenreID', on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.metagenre')),
                ('tvshowid', models.ForeignKey(db_column='TVShowID', on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.tvshow')),
            ],
            options={
                'db_table': 'TVGenre',
            },
        ),
    ]
