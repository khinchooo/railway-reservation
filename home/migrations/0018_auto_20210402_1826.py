# Generated by Django 3.1.7 on 2021-04-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210402_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_no',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]