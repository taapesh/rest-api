# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0006_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ownerId', models.IntegerField(default=-1)),
                ('customerId', models.IntegerField(default=-1)),
                ('customerEmail', models.CharField(default=b'', max_length=255)),
                ('customerFirstName', models.CharField(default=b'', max_length=255)),
                ('customerLastName', models.CharField(default=b'', max_length=255)),
                ('orderPrice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('orderName', models.CharField(default=b'', max_length=255)),
                ('restaurantAddress', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='table',
            name='address',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='table',
            name='tableNum',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='table',
            name='ownerEmail',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='table',
            name='ownerFirstName',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='table',
            name='ownerLastName',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
