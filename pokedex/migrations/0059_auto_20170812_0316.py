# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-12 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0058_adopt_park_adopt'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunt',
            name='second_hatched',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hunt',
            name='second_pokemon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_hunting_pokemon', to='pokedex.Pokemon'),
        ),
    ]
