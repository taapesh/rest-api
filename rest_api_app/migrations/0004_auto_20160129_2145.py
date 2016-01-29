# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0003_auto_20160129_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='party_size',
            field=models.IntegerField(default=1),
        ),
    ]
