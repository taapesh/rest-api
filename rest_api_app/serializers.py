from rest_framework import serializers
from models import MyUser, Table, Order, Receipt

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            "server_id",
            "party_size",
            "address_table_combo",
            "request_made",
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            "first_name",
        )

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            "id",
            "customer_id",
            "order_name",
            "order_price",
            "customer_first_name",
            "table_number",
            "restaurant_address",
            "address_table_combo",
            "receipt_id",
        )

class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = (
            "customer_id",
            "total_bill",
            "restaurant_name",
            "restaurant_address",
            "server_name",
            "server_rating",
        )
        