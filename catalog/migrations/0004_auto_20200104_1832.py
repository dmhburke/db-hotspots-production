# Generated by Django 2.2.1 on 2020-01-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_singlelocationrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanreviewmodel',
            name='count_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='ave_ratings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='count_ratings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='singlelocationrecord',
            name='count_wishlist',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]