# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import election.models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0006_auto_20160130_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='key',
            field=models.IntegerField(default=election.models.generate_random_voter_key),
        ),
        migrations.AlterField(
            model_name='election',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='election',
            name='is_finished',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='election',
            name='name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='historicalelection',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='historicalelection',
            name='is_finished',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='historicalelection',
            name='name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='voter',
            name='roll_no',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voted',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]