# Generated by Django 4.2.4 on 2024-04-11 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0117_remove_movie_change_movie_changeurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tvcrew',
            fields=[
                ('tvcrewid', models.AutoField(db_column='TVCrewID', primary_key=True, serialize=False)),
                ('characterid', models.ForeignKey(blank=True, db_column='CharacterID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.charactermeta')),
                ('peopleid', models.ForeignKey(db_column='PeopleID', on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.creator')),
                ('roleid', models.ForeignKey(db_column='RoleID', on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.creatorrole')),
                ('tvshowid', models.ForeignKey(db_column='TVShowID', on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.tvshow')),
            ],
            options={
                'db_table': 'TVCrew',
            },
        ),
    ]
