# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0005_auto_20160129_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
    ]
