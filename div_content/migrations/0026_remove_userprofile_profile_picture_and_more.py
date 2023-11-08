# Generated by Django 4.2.4 on 2023-10-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0025_userprofile_birthdate_userprofile_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profilepicture',
            field=models.ImageField(blank=True, db_column='ProfilePicture', null=True, upload_to='img/profiles/2023/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, db_column='Bio'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(blank=True, db_column='BirthDate', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, db_column='Location', max_length=255),
        ),
    ]
