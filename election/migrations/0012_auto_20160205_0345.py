# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0011_auto_20160204_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
