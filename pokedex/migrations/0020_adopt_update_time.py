# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-22 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0019_pokemon_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopt',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
