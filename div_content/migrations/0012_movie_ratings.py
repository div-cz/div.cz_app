# Generated by Django 4.2.4 on 2023-10-16 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
        ('div_content', '0011_remove_movie_titlecz3'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]