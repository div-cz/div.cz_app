# Generated by Django 4.2.4 on 2023-10-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0019_alter_charactermeta_characterid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterbook',
            name='bookcharacterid',
            field=models.IntegerField(blank=True, db_column='BookCharacterID', null=True),
        ),
        migrations.AlterField(
            model_name='charactermeta',
            name='characterid',
            field=models.IntegerField(db_column='CharacterID', default=1),
            preserve_default=False,
        ),
    ]