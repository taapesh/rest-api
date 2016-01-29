from rest_framework import serializers
from models import Table

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            'id',
            'timeCreated',
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
            'tableNumber',
            'restaurantAddress',
        )
