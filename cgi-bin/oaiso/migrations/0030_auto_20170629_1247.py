# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0029_auto_20170629_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='shop',
        ),
        migrations.AlterField(
            model_name='genre',
            name='shop_relation',
            field=models.ManyToManyField(to='oaiso.Shop'),
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
