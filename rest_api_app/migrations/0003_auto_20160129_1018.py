# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0002_auto_20160129_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='active_table_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='table',
            name='restaurantAddress',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
