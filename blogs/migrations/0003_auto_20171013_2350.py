# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20171013_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]