from rest_framework import serializers
from models import Table, MyUser

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            "server_id",
            "party_size",
            "address_table_combo",
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            "first_name",
        )