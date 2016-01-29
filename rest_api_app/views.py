from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from rest_api_app.models import Table, MyUser
from rest_api_app.serializers import TableSerializer, UserSerializer

@api_view(['POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def create_or_join_table(request):
    # Find server id to assign
    restaurant_address = request.data.get("restaurant_address")
    table_number = request.data.get("table_number")
    address_table_combo = request.data.get('address_table_combo')
    server_id = find_server(restaurant_address)

    # Attempt to create table, if does not exist
    table, created = Table.objects.get_or_create(
        address_table_combo=address_table_combo,
        defaults={"server_id": server_id}
    )
    table.party_size += 1
    table.save()

    user = MyUser.objects.get(id=request.data.get("user_id"))
    user.address_table_combo = address_table_combo
    user.active_table_number = table_number
    user.active_restaurant = restaurant_address
    user.save()
    
    return Response({
        "message": "Joined table",
        "party_size": table.party_size
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def delete_table(request):
    try:
        table = Table.objects.get(address_table_combo=request.data.get('address_table_combo'))
    except Table.DoesNotExist:
        return Response({"error":"Table does not exist"}, status=status.HTTP_404_NOT_FOUND)
    table.delete()
    return Response({"success": "Table deleted"}, status=status.HTTP_200_OK)

@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_all_tables(request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_users_at_table(request):
    users = MyUser.objects.all().filter(address_table_combo=request.data.get('address_table_combo'))
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def find_server(restaurant_address):
    return 1

