# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='auto_generated',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]