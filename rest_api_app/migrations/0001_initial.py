# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(default=b'', max_length=255)),
                ('last_name', models.CharField(default=b'', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ownerId', models.IntegerField(default=-1)),
                ('serverId', models.IntegerField(default=-1)),
                ('partySize', models.IntegerField(default=1)),
                ('ownerEmail', models.CharField(default=b'', max_length=255)),
                ('ownerFirstName', models.CharField(default=b'', max_length=255)),
                ('ownerLastName', models.CharField(default=b'', max_length=255)),
                ('requestMade', models.BooleanField(default=False)),
                ('timeOfRequest', models.IntegerField(default=-1)),
                ('isFinished', models.BooleanField(default=False)),
                ('timeOfFinish', models.IntegerField(default=-1)),
                ('viewIdx', models.IntegerField(default=-1)),
                ('address', models.CharField(default=b'', max_length=255)),
                ('tableNum', models.IntegerField(default=-1)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
