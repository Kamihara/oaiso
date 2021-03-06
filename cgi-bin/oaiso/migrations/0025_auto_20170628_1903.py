# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0024_genreship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genreship',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='genreship',
            old_name='shop_id',
            new_name='shop',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='shop_id',
            new_name='shop',
        ),
        migrations.AddField(
            model_name='genre',
            name='shop_genre',
            field=models.ManyToManyField(through='oaiso.Genreship', to='oaiso.Shop'),
        ),
    ]
