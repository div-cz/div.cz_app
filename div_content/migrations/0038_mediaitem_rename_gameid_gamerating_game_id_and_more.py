# Generated by Django 4.2.4 on 2023-10-01 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0037_remove_article_article_remove_creator_nationality_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('media_item_id', models.AutoField(db_column='MediaItemID', primary_key=True, serialize=False)),
                ('media_type', models.IntegerField(choices=[('1', 'Book'), ('2', 'Game'), ('3', 'Movie')], db_column='MediaType')),
                ('role', models.IntegerField(choices=[('1', 'Main'), ('2', 'Side'), ('3', 'Prop')], db_column='Role')),
                ('media_id', models.IntegerField(db_column='MediaID')),
            ],
            options={
                'db_table': 'MediaItem',
            },
        ),
        migrations.RenameField(
            model_name='gamerating',
            old_name='gameid',
            new_name='game_id',
        ),
        migrations.RenameField(
            model_name='gamerating',
            old_name='ratingid',
            new_name='rating_id',
        ),
        migrations.RenameField(
            model_name='gamerating',
            old_name='userid',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itemdescription',
            new_name='item_description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itemid',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itemname',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itemnamecz',
            new_name='item_name_cz',
        ),
        migrations.RenameField(
            model_name='itemgame',
            old_name='gameid',
            new_name='game_id',
        ),
        migrations.RenameField(
            model_name='itemgame',
            old_name='gameitemid',
            new_name='game_item_id',
        ),
        migrations.RenameField(
            model_name='itemgame',
            old_name='itemid',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='itemgame',
            old_name='itemrole',
            new_name='item_role',
        ),
        migrations.RenameField(
            model_name='itemmovie',
            old_name='itemid',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='itemmovie',
            old_name='itemrole',
            new_name='item_role',
        ),
        migrations.RenameField(
            model_name='itemmovie',
            old_name='movieid',
            new_name='movie_id',
        ),
        migrations.RenameField(
            model_name='itemmovie',
            old_name='movieitemid',
            new_name='movie_item_id',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='locationadress',
            new_name='location_adress',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='locationdescription',
            new_name='location_description',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='locationid',
            new_name='location_id',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='locationname',
            new_name='location_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='locationtype',
            new_name='location_type',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='parentlocationid',
            new_name='parent_location_id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemtypeid',
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(blank=True, choices=[('1', 'Zbraň'), ('2', 'Nástroj'), ('3', 'Oděv'), ('4', 'Vozidlo'), ('5', 'Dokument'), ('6', 'Klenot'), ('7', 'Domácí potřeby'), ('8', 'Magický předmět'), ('9', 'Artefakt'), ('10', 'Ostatní')], db_column='ItemType', max_length=3, null=True),
        ),
        migrations.DeleteModel(
            name='Itemtypes',
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='item',
            field=models.ForeignKey(db_column='Item', on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.item'),
        ),
    ]
