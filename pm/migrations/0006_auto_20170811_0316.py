# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-11 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0005_pm_parent_pm'),
    ]

    operations = [
        migrations.AddField(
            model_name='pm',
            name='deleted_by_receiver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pm',
            name='deleted_by_sender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pm',
            name='replied',
            field=models.BooleanField(default=False),
        ),
    ]