# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complexname',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complexname',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='amenity',
            field=models.ManyToManyField(blank=True, to='main.Amenities'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]