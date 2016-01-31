from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from rest_api_app.models import Table, MyUser, Order, TableRequest, Receipt, MyUserManager
from rest_api_app.serializers import UserSerializer, TableSerializer, OrderSerializer, ReceiptSerializer

from django.db.models import Sum
from django.db.models import F

from django.db import IntegrityError

@api_view()
def api_root(request):
    """ tablemate API """
    return Response({
        "login": "http://127.0.0.1:8000/login/"
    })

@api_view(["GET"])
def get_all_users(request):
    users = MyUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        user = MyUser.objects.get(email=email)
        if user.check_password(password):
            token = Token.objects.get_or_create(user=user)
            
            return Response({
                "auth_token": token[0].key,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "user_id": user.id
            }, status=status.HTTP_200_OK)

    except MyUser.DoesNotExist:
        return Response({"error": "There was a problem"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response({"success": "Logged out successfully"})

@api_view(["POST"])
def register(request):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    password = request.data.get("password")
    
    try:
        user = MyUser.objects.create_user(first_name, last_name, email, password)
        token = Token.objects.get_or_create(user=user)

        return Response({
            "auth_token": token[0].key,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "user_id": user.id
        }, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response({"error": "Email is already in use"}, status=status.HTTP_409_CONFLICT)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_info(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_or_join_table(request):
    # Find server id to assign
    address_table_combo = request.data.get("address_table_combo")
    restaurant_address = request.data.get("restaurant_address")
    restaurant_name = request.data.get("restaurant_name")
    server_id = find_server(restaurant_address)

    # Attempt to create table, if does not exist
    table, created = Table.objects.get_or_create(
        address_table_combo=address_table_combo,
    )
    if not created:
        table.party_size += 1
    else:
        table.server_id = server_id
        table.restaurant_name = restaurant_name
    table.save()

    MyUser.objects.filter(id=request.data.get("user_id")).update(
        address_table_combo=address_table_combo,
        active_table_number=request.data.get("table_number"),
        active_restaurant=restaurant_address
    )
    
    return Response({
        "message": "Joined table",
        "party_size": table.party_size,
        "restaurant_name": table.restaurant_name
    }, status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def delete_table(request):
    Table.objects.filter(address_table_combo=request.data.get("address_table_combo")).delete()
    return Response({"success": "Table deleted"}, status=status.HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_all_tables(request):
    serializer = TableSerializer(Table.objects.all(), many=True)
    return Response(serializer.data)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_server_tables(request):
    tables = Table.objects.filter(server_id=request.data.get("user_id"))
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_users_at_table(request):
    users = MyUser.objects.filter(address_table_combo=request.data.get("address_table_combo"))
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def request_service(request):
    table_request, created = TableRequest.objects.get_or_create(
        address_table_combo=request.data.get("address_table_combo"),
    )
    if created:
        return Response({"success": "Request made"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Request already made"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def serve_request(request):
    TableRequest.objects.filter(address_table_combo=request.data.get("address_table_combo")).delete()
    return Response({"success": "Request served"}, status=status.HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def has_request(request):
    return Response({
        "request_made": TableRequest.objects
        .filter(address_table_combo=request.data.get("address_table_combo"))
        .exists()
    })

def find_server(restaurant_address):
    return 1

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
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
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def queue_order(request):
    Order.objects.get(id=request.data.get("id")).update(new_order=False, order_queued=True)
    return Response({"message": "Order queued"}, status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def order_delivered(request):
    Order.objects.get(id=request.data.get("id")).update(order_queued=False, payment_pending=True)
    return Response({"message": "Order delivered, payment pending"}, status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def finish_and_pay(request):
    address_table_combo = request.data.get("address_table_combo")
    table = get_table(address_table_combo)

    if table is None:
        return Response({"error": "Table does not exist"}, status=status.HTTP_404_NOT_FOUND)

    user_id = request.data.get("user_id")
    orders = Order.objects.filter(
        customer_id=user_id, address_table_combo=address_table_combo, active_order=True)

    total = 0.00
    if orders.exists():
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

    return Response({"message": "Payment successful", "bill": total}, status=status.HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
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
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_receipts(request):
    receipts = Receipt.objects.filter(customer_id=request.data.get("user_id"))
    serializer = ReceiptSerializer(receipts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_orders(request):
    orders = Order.objects.filter(customer_id=request.data.get("user_id"))
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_test_server(request):
    first_name = "William"
    last_name = "Woodhouse"
    email = "woodhouse@gmail.com"
    password = "12345"
    
    try:
        user = MyUser.objects.create_user(first_name, last_name, email, password)
        user.is_server = True
        user.is_working = True
        user.working_restaurant = "1234 Restaurant St."
        token = Token.objects.get_or_create(user=user)

        return Response({
            "auth_token": token[0].key,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "user_id": user.id
        }, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response({"error": "Email is already in use"}, status=status.HTTP_409_CONFLICT)
