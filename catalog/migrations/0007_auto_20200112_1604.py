# Generated by Django 2.2.1 on 2020-01-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200105_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masteraddmodel',
            name='temperature',
        ),
        migrations.AddField(
            model_name='masteraddmodel',
            name='lat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='masteraddmodel',
            name='long',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
