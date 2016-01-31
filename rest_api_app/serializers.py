from rest_framework import serializers
from models import MyUser, Table, Order, Receipt

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            "server_id",
            "server_name",
            "party_size",
            "address_table_combo",
            "request_made",
            "restaurant_name",
            "restaurant_address",
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "active_table_number",
            "active_restaurant",
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
