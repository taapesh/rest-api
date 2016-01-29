# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0004_auto_20160129_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='active_table_id',
            new_name='active_table_number',
        ),
        migrations.RemoveField(
            model_name='table',
            name='owner_email',
        ),
        migrations.RemoveField(
            model_name='table',
            name='owner_first_name',
        ),
        migrations.RemoveField(
            model_name='table',
            name='owner_last_name',
        ),
        migrations.RemoveField(
            model_name='table',
            name='restaurant_address',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_number',
        ),
        migrations.AddField(
            model_name='myuser',
            name='active_restaurant',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='myuser',
            name='address_table_combo',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='table',
            name='address_table_combo',
            field=models.CharField(default=b'', unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='table',
            name='party_size',
            field=models.IntegerField(default=0),
        ),
    ]
