# Generated by Django 2.0.4 on 2018-04-23 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180423_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='botcommandentry',
            name='entry_lang',
            field=models.CharField(default='es', max_length=5, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='botcommandentry',
            name='allows_pm',
            field=models.BooleanField(default=True, verbose_name='Allows PM'),
        ),
        migrations.AlterUniqueTogether(
            name='botcommandentry',
            unique_together={('name', 'entry_lang')},
        ),
    ]
