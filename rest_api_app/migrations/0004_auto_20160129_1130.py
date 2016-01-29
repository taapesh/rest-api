# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0003_auto_20160129_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ('time_created',)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerEmail',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerFirstName',
            new_name='customer_first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerId',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerLastName',
            new_name='customer_last_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderName',
            new_name='order_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderPrice',
            new_name='order_price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ownerId',
            new_name='owner_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='restaurantAddress',
            new_name='restaurant_address',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='isFinished',
            new_name='is_finished',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='ownerEmail',
            new_name='owner_email',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='ownerFirstName',
            new_name='owner_first_name',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='ownerId',
            new_name='owner_id',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='ownerLastName',
            new_name='owner_last_name',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='partySize',
            new_name='party_size',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='requestMade',
            new_name='request_made',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='restaurantAddress',
            new_name='restaurant_address',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='serverId',
            new_name='server_id',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='tableNumber',
            new_name='table_number',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='timeCreated',
            new_name='time_created',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='timeOfFinish',
            new_name='time_of_finish',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='timeOfRequest',
            new_name='time_of_request',
        ),
    ]
