# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0050_auto_20170704_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
