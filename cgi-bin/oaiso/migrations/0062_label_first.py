# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0061_auto_20171013_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label_first',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_cheap', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('budget_reasonable', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('budget_expensive', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('priority_food', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('priority_drink', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('priority_atmosphere', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('priority_speed', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('can_alone', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
                ('cannot_alone', models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True)),
            ],
        ),
    ]
