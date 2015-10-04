# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
