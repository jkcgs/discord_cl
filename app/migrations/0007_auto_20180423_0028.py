# Generated by Django 2.0.4 on 2018-04-23 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180423_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botcommandentry',
            name='aliases',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='config_help',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='usage',
            field=models.TextField(default='', null=True),
        ),
    ]
