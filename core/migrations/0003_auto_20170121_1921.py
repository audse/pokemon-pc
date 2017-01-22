# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-22 01:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_action_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('category', models.CharField(max_length=140)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
