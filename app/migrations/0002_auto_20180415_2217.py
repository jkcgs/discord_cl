# Generated by Django 2.0.4 on 2018-04-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordadmin',
            name='userid',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]