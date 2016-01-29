# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0004_auto_20160129_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_of_request', models.DateTimeField(auto_now_add=True)),
                ('address_table_combo', models.CharField(default=b'', unique=True, max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created',
            new_name='time_created',
        ),
    ]
