# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 05:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0016_alter_field_indicator_on_target_allow_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goals/goals/images', verbose_name='Image')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('extras', django.contrib.postgres.fields.hstore.HStoreField(blank=True, default={}, null=True, verbose_name='Extras')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.AddField(
            model_name='goal',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='goals.Plan', verbose_name='plan'),
        ),
    ]
