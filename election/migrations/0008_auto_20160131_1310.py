# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0007_auto_20160131_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='is_key_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalelection',
            name='is_key_required',
            field=models.BooleanField(default=True),
        ),
    ]
