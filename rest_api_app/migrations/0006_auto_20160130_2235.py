# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0005_auto_20160129_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='total_bill',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
        ),
    ]
