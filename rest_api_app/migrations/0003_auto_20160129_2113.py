# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0002_auto_20160129_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='visit_id',
            new_name='receipt_id',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='receipt',
            name='server_rating',
            field=models.IntegerField(default=-1),
        ),
    ]
