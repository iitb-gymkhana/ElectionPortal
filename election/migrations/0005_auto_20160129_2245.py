# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_historicalelection'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='is_temporary_closed',
            field=models.BooleanField(default=False, help_text='Election temporary closed'),
        ),
        migrations.AddField(
            model_name='historicalelection',
            name='is_temporary_closed',
            field=models.BooleanField(default=False, help_text='Election temporary closed'),
        ),
    ]
