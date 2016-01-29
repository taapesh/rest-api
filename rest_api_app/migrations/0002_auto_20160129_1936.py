# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_queued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant_address',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
