# Generated by Django 4.2.4 on 2023-10-14 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('div_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcomments',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookpurchase',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookrating',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creatorbiography',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gamecomments',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gamepurchase',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gamerating',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='adult',
            field=models.CharField(db_column='Adult', max_length=1),
        ),
        migrations.AlterField(
            model_name='moviecomments',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movierating',
            name='userid',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]