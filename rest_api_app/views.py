from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from rest_api_app.models import Table, MyUser, Order, TableRequest, Receipt
from rest_api_app.serializers import UserSerializer, TableSerializer, OrderSerializer, ReceiptSerializer

from django.db.models import Sum
from django.db.models import F

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def create_or_join_table(request):
    # Find server id to assign
    address_table_combo = request.data.get("address_table_combo")
    restaurant_address = request.data.get("restaurant_address")
    server_id = find_server(restaurant_address)

    # Attempt to create table, if does not exist
    table, created = Table.objects.get_or_create(
        address_table_combo=address_table_combo,
    )
    if not created:
        table.party_size += 1
    else:
        table.server_id = server_id
    table.save()

    MyUser.objects.filter(id=request.data.get("user_id")).update(
        address_table_combo=address_table_combo,
        active_table_number=request.data.get("table_number"),
        active_restaurant=restaurant_address
    )
    
    return Response({
        "message": "Joined table",
        "party_size": table.party_size
    }, status=status.HTTP_200_OK)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def delete_table(request):
    Table.objects.filter(address_table_combo=request.data.get("address_table_combo")).delete()
    return Response({"success": "Table deleted"}, status=status.HTTP_200_OK)

@api_view(["GET"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_all_tables(request):
    serializer = TableSerializer(Table.objects.all(), many=True)
    return Response(serializer.data)

@api_view(["GET"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_users_at_table(request):
    users = MyUser.objects.filter(address_table_combo=request.data.get("address_table_combo"))
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def request_service(request):
    table_request, created = TableRequest.objects.get_or_create(
        address_table_combo=request.data.get("address_table_combo"),
    )
    if created:
        return Response({"success": "Request made"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Request already made"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def serve_request(request):
    TableRequest.objects.filter(address_table_combo=request.data.get("address_table_combo")).delete()
    return Response({"success": "Request served"}, status=status.HTTP_200_OK)

@api_view(["GET"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def has_request(request):
    return Response({
        "request_made": TableRequest.objects
        .filter(address_table_combo=request.data.get("address_table_combo"))
        .exists()
    })

def find_server(restaurant_address):
    return 1

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def place_order(request):
    """ Provide order_name, order_price, customer_first_name, address_table_combo, restaurant_address table_number """
    # Check if table exists first?

    serializer = OrderSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def queue_order(request):
    Order.objects.get(id=request.data.get("id")).update(new_order=False, order_queued=True)
    return Response({"message": "Order queued"}, status=status.HTTP_200_OK)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def order_delivered(request):
    Order.objects.get(id=request.data.get("id")).update(order_queued=False, payment_pending=True)
    return Response({"message": "Order delivered, payment pending"}, status=status.HTTP_200_OK)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def finish_and_pay(request):
    address_table_combo = request.data.get("address_table_combo")
    table = get_table(address_table_combo)

    if table is None:
        return Response({"error": "Table does not exist"}, status=status.HTTP_404_NOT_FOUND)

    user_id = request.data.get("user_id")
    orders = Order.objects.filter(
        customer_id=user_id, address_table_combo=address_table_combo, active_order=True)

    total = 0.00
    if orders:
        subtotal = orders.aggregate(Sum("order_price")).get("order_price__sum", 0.00)

        # Add tax, attempt payment
        total = subtotal

        # If payment successful
    
    # Assuming payment was successful
    table.party_size -= 1
    table.save()
    """
    if table.party_size == 0:
        table.delete()
    """    

    receipt = Receipt(
        customer_id=user_id,
        total_bill=total,
        server_name=request.data.get("server_name"),
        restaurant_name=request.data.get("restaurant_name"),
        restaurant_address=request.data.get("restaurant_address"),
        server_rating=request.data.get("server_rating", -1)
    )
    receipt.save()
    orders.update(payment_pending=False, active_order=False, receipt_id=receipt.id)
    
    """
    Order.objects
        .filter(customer_id=customer_id)
        .filter(address_table_combo=address_table_combo)
        .filter(active_order=True)
        .update(payment_pending=False, active_order=False, receipt_id=receipt.id)
    """
    return Response({"message": "Payment successful", "bill": total}, status=status.HTTP_200_OK)


@api_view(["GET"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_table_orders(request):
    address_table_combo = request.data.get("address_table_combo")
    orders = Order.objects.filter(address_table_combo=address_table_combo, active_order=True)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

def get_table(address_table_combo):
    try:
        table = Table.objects.get(address_table_combo=address_table_combo)
        return table
    except Table.DoesNotExist:
        None

@api_view(["GET"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_receipts(request):
    receipts = Receipt.objects.filter(customer_id=request.data.get("user_id"))
    serializer = ReceiptSerializer(receipts, many=True)
    return Response(serializer.data)

@api_view(["POST"])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def delete_all_orders(request):
    Order.objects.all().delete()
    return Response({"success": "Deleted orders"})

