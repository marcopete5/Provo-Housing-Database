# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160219_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='distance_from_BYU',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='distance_from_UVU',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]
