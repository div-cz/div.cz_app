# Generated by Django 4.2.4 on 2023-09-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0008_movie_img_alter_movie_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='googleid',
            field=models.CharField(db_column='GoogleID', max_length=16, null=True),
        ),
    ]