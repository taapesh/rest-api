# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0002_remove_table_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_server',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_working',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='num_server_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='server_rating',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='myuser',
            name='working_restaurant',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
