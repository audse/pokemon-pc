# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-11 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0054_adopt_evolved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopt',
            name='box_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]