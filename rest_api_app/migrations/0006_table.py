# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0005_myuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ownerId', models.IntegerField(default=-1)),
                ('serverId', models.IntegerField(default=-1)),
                ('partySize', models.IntegerField(default=1)),
                ('ownerEmail', models.CharField(max_length=255)),
                ('ownerFirstName', models.CharField(max_length=255)),
                ('ownerLastName', models.CharField(max_length=255)),
                ('viewIdx', models.IntegerField(default=-1)),
                ('requestMade', models.BooleanField(default=False)),
                ('timeOfRequest', models.IntegerField(default=-1)),
                ('isFinished', models.BooleanField(default=False)),
                ('timeOfFinish', models.IntegerField(default=-1)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
