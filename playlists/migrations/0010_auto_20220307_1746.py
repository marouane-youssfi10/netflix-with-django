# Generated by Django 3.1.3 on 2022-03-07 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0009_movieproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieproxy',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]