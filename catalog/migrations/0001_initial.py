# Generated by Django 2.2.1 on 2020-01-03 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='profilepictures')),
                ('homecity', models.CharField(blank=True, max_length=30, null=True)),
                ('number_rating', models.IntegerField(blank=True, null=True)),
                ('high_rating', models.CharField(blank=True, max_length=45, null=True)),
                ('last_rating', models.CharField(blank=True, max_length=45, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]