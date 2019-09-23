# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 16:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='casted_at',
        ),
        migrations.AddField(
            model_name='votesession',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 13, 16, 52, 44, 447220, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='vote.VoteSession'),
        ),
    ]
