# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-16 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='coordinates',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
