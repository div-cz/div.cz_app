# Generated by Django 4.2.4 on 2023-12-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0075_alter_bookauthor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pseudonym',
            field=models.CharField(blank=True, db_column='Pseudonym', max_length=2, null=True),
        ),
    ]