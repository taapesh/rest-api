from rest_framework import serializers
from models import Table, Order

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            'created',
            'ownerId',
            'serverId',
            'partySize',
            'ownerEmail',
            'ownerFirstName',
            'ownerLastName',
            'requestMade',
            'timeOfRequest',
            'isFinished',
            'timeOfFinish',
            'viewIdx',
            'address',
            'tableNum',
        )

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'customerId',
            'ownerId',
        )
