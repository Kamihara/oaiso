# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0054_merge_20170704_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='shop_relation',
            field=models.ManyToManyField(to='oaiso.Shop'),
        ),
    ]
