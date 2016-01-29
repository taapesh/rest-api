# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0005_auto_20160129_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='new_table',
            field=models.BooleanField(default=False),
        ),
    ]
