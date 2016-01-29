# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ('timeCreated',)},
        ),
        migrations.RenameField(
            model_name='table',
            old_name='tableNum',
            new_name='tableNumber',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='created',
            new_name='timeCreated',
        ),
        migrations.RemoveField(
            model_name='table',
            name='address',
        ),
        migrations.RemoveField(
            model_name='table',
            name='viewIdx',
        ),
    ]
