# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-26 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os2webscanner', '0007_auto_20180426_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='filescanner',
            name='is_running',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='webscanner',
            name='is_running',
            field=models.BooleanField(default=False),
        ),
    ]
