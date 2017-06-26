# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0017_create_model_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='level',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='lft',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='goals.Area'),
        ),
        migrations.AddField(
            model_name='area',
            name='rght',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
    ]
