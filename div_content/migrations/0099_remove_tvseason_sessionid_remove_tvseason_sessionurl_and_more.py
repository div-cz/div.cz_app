# Generated by Django 4.2.4 on 2024-04-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0098_remove_tvseason_seassonname_tvepisode_titlecz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvseason',
            name='sessionid',
        ),
        migrations.RemoveField(
            model_name='tvseason',
            name='sessionurl',
        ),
        migrations.AddField(
            model_name='tvseason',
            name='seasonid',
            field=models.IntegerField(db_column='SeasonID', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tvseason',
            name='seasonurl',
            field=models.CharField(blank=True, db_column='SeasonURL', max_length=255, null=True),
        ),
    ]
