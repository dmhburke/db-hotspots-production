# Generated by Django 2.2.1 on 2020-02-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20200214_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_big_group',
            field=models.BooleanField(default=False, verbose_name='single_pf_big_group'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_breakfast',
            field=models.BooleanField(default=False, verbose_name='single_pf_breakfast'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_date_night',
            field=models.BooleanField(default=False, verbose_name='single_pf_date_night'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_impressing_guests',
            field=models.BooleanField(default=False, verbose_name='single_pf_impressing guests'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_last_min_dinner',
            field=models.BooleanField(default=False, verbose_name='single_pf_last_min_dinner'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_living_large',
            field=models.BooleanField(default=False, verbose_name='single_pf_living_large'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_peace_quiet',
            field=models.BooleanField(default=False, verbose_name='single_pf_peace_quiet'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_quick_lunch',
            field=models.BooleanField(default=False, verbose_name='single_pf_quick_lunch'),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='pf_sunny_days',
            field=models.BooleanField(default=False, verbose_name='single_pf_sunny_days'),
        ),
    ]
