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
                ('active_table_number', models.IntegerField(default=-1)),
                ('active_restaurant', models.CharField(default=b'', max_length=255)),
                ('address_table_combo', models.CharField(default=b'', max_length=255)),
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
                ('order_name', models.CharField(default=b'', max_length=255)),
                ('order_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('customer_first_name', models.CharField(default=b'', max_length=255)),
                ('address_table_combo', models.CharField(default=b'', max_length=255)),
                ('table_number', models.IntegerField(default=-1)),
                ('new_order', models.BooleanField(default=True)),
                ('active_order', models.BooleanField(default=True)),
                ('visit_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_id', models.IntegerField(default=-1)),
                ('restaurant_name', models.CharField(default=b'', max_length=255)),
                ('restaurant_address', models.CharField(default=b'', max_length=255)),
                ('server_name', models.CharField(default=b'', max_length=255)),
                ('total_bill', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('owner_id', models.IntegerField(default=-1)),
                ('server_id', models.IntegerField(default=-1)),
                ('party_size', models.IntegerField(default=0)),
                ('request_made', models.BooleanField(default=False)),
                ('time_of_request', models.IntegerField(default=-1)),
                ('is_finished', models.BooleanField(default=False)),
                ('time_of_finish', models.IntegerField(default=-1)),
                ('address_table_combo', models.CharField(default=b'', unique=True, max_length=255)),
                ('restaurant_name', models.CharField(default=b'', max_length=255)),
                ('new_table', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('time_created',),
            },
        ),
    ]
