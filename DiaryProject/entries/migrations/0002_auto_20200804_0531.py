# Generated by Django 3.0 on 2020-08-04 05:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='entries',
            new_name='Entry',
        ),
    ]