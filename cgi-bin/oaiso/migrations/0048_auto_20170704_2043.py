# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0047_auto_20170704_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_name',
            field=models.TextField(),
        ),
    ]
