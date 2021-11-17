# Generated by Django 3.2.9 on 2021-11-17 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_auto_20211117_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='album',
            new_name='army_name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='unit_name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='nationality',
            new_name='unit_stats',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='photo_url',
            new_name='unit_upgrades',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='title',
        ),
    ]
