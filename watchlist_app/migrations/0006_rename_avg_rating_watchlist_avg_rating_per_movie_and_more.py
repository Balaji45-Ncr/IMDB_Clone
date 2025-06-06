# Generated by Django 4.2.11 on 2025-05-22 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_watchlist_total_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='avg_rating',
            new_name='avg_rating_per_movie',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='number_ratings',
            new_name='number_of_ratings_per_movie',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='total_ratings',
            new_name='total_avg_ratings',
        ),
    ]
