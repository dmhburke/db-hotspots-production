# Generated by Django 2.2.1 on 2020-01-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200112_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlelocationrecord',
            name='lat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='singlelocationrecord',
            name='long',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
