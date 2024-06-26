# Generated by Django 4.2.4 on 2023-12-30 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('div_content', '0078_book_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authorid',
            field=models.ForeignKey(db_column='AuthorID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='div_content.bookauthor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.CharField(db_column='URL', max_length=255),
        ),
    ]
