# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-22 21:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0020_adopt_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopt',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 22, 21, 14, 31, 609826, tzinfo=utc)),
        ),
    ]
