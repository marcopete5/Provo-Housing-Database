# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160216_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='name',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]