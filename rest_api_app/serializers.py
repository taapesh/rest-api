from rest_framework import serializers
from models import Table, MyUser

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            'id',
            'time_created',
            'owner_id',
            'server_id',
            'party_size',
            'owner_email',
            'owner_first_name',
            'owner_last_name',
            'request_made',
            'time_of_request',
            'is_finished',
            'time_of_finish',
            'table_number',
            'restaurant_address',
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'first_name',
        )