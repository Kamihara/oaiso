# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0056_auto_20170904_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.TextField(blank=True, null=True)),
                ('lat', models.DecimalField(decimal_places=13, max_digits=16)),
                ('lng', models.DecimalField(decimal_places=13, max_digits=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='shop',
            name='budget_2',
        ),
    ]
