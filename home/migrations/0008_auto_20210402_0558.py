# Generated by Django 3.1.7 on 2021-04-01 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210401_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='end_station',
            new_name='e_station',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='start_station',
            new_name='s_station',
        ),
    ]