# Generated by Django 2.2.1 on 2020-02-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20200207_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_big_group',
            field=models.BooleanField(default=False, verbose_name='pf_big_group'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_breakfast',
            field=models.BooleanField(default=False, verbose_name='pf_breakfast'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_date_night',
            field=models.BooleanField(default=False, verbose_name='pf_date_night'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_impressing_guests',
            field=models.BooleanField(default=False, verbose_name='pf_impressing guests'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_last_min_dinner',
            field=models.BooleanField(default=False, verbose_name='pf_last_min_dinner'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_living_large',
            field=models.BooleanField(default=False, verbose_name='pf_living_large'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_peace_quiet',
            field=models.BooleanField(default=False, verbose_name='pf_peace_quiet'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_quick_lunch',
            field=models.BooleanField(default=False, verbose_name='pf_quick_lunch'),
        ),
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='pf_sunny_days',
            field=models.BooleanField(default=False, verbose_name='pf_sunny_days'),
        ),
    ]
