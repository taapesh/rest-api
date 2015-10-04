# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0003_myuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='phone',
        ),
    ]
