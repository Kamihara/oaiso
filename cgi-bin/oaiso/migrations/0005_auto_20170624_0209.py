# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0004_auto_20170624_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='hpg_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='ret_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='tab_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
