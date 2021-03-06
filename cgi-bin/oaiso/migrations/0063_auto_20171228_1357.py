# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-28 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0062_label_first'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.TextField(blank=True, null=True)),
                ('oaiso_genre', models.TextField(blank=True, null=True)),
                ('genre', models.TextField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('tel', models.TextField(blank=True, null=True)),
                ('bussiness_hours', models.TextField(blank=True, null=True)),
                ('photo_food', models.TextField(blank=True, null=True)),
                ('photo_shop', models.TextField(blank=True, null=True)),
                ('budget_lunch_min', models.TextField(blank=True, null=True)),
                ('budget_lunch_max', models.TextField(blank=True, null=True)),
                ('budget_dinner_min', models.TextField(blank=True, null=True)),
                ('budget_dinner_max', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_cheap', models.FloatField(blank=True, null=True)),
                ('budget_reasonable', models.FloatField(blank=True, null=True)),
                ('budget_expensive', models.FloatField(blank=True, null=True)),
                ('priority_food', models.FloatField(blank=True, null=True)),
                ('priority_drink', models.FloatField(blank=True, null=True)),
                ('priority_atmosphere', models.FloatField(blank=True, null=True)),
                ('priority_speed', models.FloatField(blank=True, null=True)),
                ('can_alone', models.FloatField(blank=True, null=True)),
                ('cannot_alone', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Shop_test',
        ),
        migrations.AlterField(
            model_name='label_first',
            name='budget_cheap',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='budget_expensive',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='budget_reasonable',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='can_alone',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='cannot_alone',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='priority_atmosphere',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='priority_drink',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='priority_food',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='label_first',
            name='priority_speed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
