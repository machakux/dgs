# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 14:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_correct_progress_value_unit_label_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Area code')),
                ('name', models.CharField(max_length=255, verbose_name='Area name')),
                ('type', models.CharField(max_length=255, verbose_name='Area type')),
                ('description', models.TextField(blank=True, verbose_name='Area description')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('extras', django.contrib.postgres.fields.hstore.HStoreField(blank=True, default={}, null=True, verbose_name='Extras')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.AddField(
            model_name='progress',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goals.Area', verbose_name='Area'),
        ),
    ]
