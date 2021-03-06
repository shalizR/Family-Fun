# Generated by Django 2.0.7 on 2018-08-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinion',
            options={},
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='opinion',
            name='awesome',
            field=models.NullBooleanField(default=False, verbose_name='awesome'),
        ),
        migrations.AddField(
            model_name='opinion',
            name='helpful',
            field=models.NullBooleanField(default=False, verbose_name='helpful'),
        ),
        migrations.AddField(
            model_name='opinion',
            name='random',
            field=models.NullBooleanField(default=False, verbose_name='random'),
        ),
    ]
