# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oaiso', '0016_auto_20170628_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shop_name', models.TextField()),
                ('budget_min', models.IntegerField(blank=True, null=True)),
                ('budget_max', models.IntegerField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('tel', models.BigIntegerField(blank=True, null=True)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('address3', models.TextField()),
                ('address4', models.TextField()),
                ('lat', models.DecimalField(decimal_places=13, max_digits=16)),
                ('lng', models.DecimalField(decimal_places=13, max_digits=16)),
            ],
        ),
        migrations.AlterField(
            model_name='genre',
            name='shop_genre',
            field=models.ManyToManyField(through='oaiso.Genreship', to='oaiso.Shop'),
        ),
        migrations.AlterField(
            model_name='genreship',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oaiso.Shop'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oaiso.Shop'),
        ),
        migrations.DeleteModel(
            name='Oaiso_Shop',
        ),
    ]
