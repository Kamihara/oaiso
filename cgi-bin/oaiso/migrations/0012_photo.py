# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0011_auto_20170627_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.BigIntegerField(blank=True, null=True)),
                ('photo_name', models.TextField()),
            ],
        ),
    ]
