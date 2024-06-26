# Generated by Django 4.2.4 on 2024-04-04 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0092_tvepisode_episodeimg_tvseason_seassonepisode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metauniversum',
            fields=[
                ('universumid', models.IntegerField(db_column='UniversumID', primary_key=True, serialize=False)),
                ('universumname', models.CharField(db_column='UniversumName', max_length=255)),
                ('universumnamecz', models.CharField(blank=True, db_column='UniversumNameCZ', max_length=255, null=True)),
                ('universumdescription', models.TextField(db_column='UniversumDescription', null=True)),
            ],
            options={
                'db_table': 'MetaUniversum',
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='worldid',
        ),
        migrations.RemoveField(
            model_name='game',
            name='worldid',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='worldid',
        ),
        migrations.DeleteModel(
            name='Metaworld',
        ),
        migrations.AddField(
            model_name='book',
            name='universumid',
            field=models.ForeignKey(db_column='UniversumID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.metauniversum'),
        ),
        migrations.AddField(
            model_name='game',
            name='universumid',
            field=models.ForeignKey(blank=True, db_column='UniversumID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.metauniversum'),
        ),
        migrations.AddField(
            model_name='movie',
            name='universumid',
            field=models.ForeignKey(blank=True, db_column='UniversumID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.metauniversum'),
        ),
    ]
