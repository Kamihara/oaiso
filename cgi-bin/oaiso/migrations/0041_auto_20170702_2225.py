# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0040_auto_20170701_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='shop_id',
            new_name='shop',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='shop_id',
        ),
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
