# Generated by Django 2.0.4 on 2018-04-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180423_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botcommandentry',
            name='aliases',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='config_help',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='usage',
            field=models.TextField(blank=True, default=''),
        ),
    ]
