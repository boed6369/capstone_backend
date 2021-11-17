# Generated by Django 3.2.9 on 2021-11-17 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0005_weapon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='army_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='unit_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='unit_stats',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='unit_upgrades',
        ),
        migrations.DeleteModel(
            name='Weapon',
        ),
    ]
