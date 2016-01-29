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
    try:
        table = Table.objects.get(restaurant_address=request.data.get('restaurant_address'))
    except Table.DoesNotExist:
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = MyUser.objects.get(id=request.data.get('user_id'))
            user.active_table_id = serializer.data.get('id')
            user.save()
            return Response({
                "message": "table created",
                "table_id": serializer.data.get('id')
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Table already exists, join it
    table.party_size += 1
    table.save()

    # Set user's active table to the table found
    user = MyUser.objects.get(id=request.data.get('user_id'))
    user.active_table_id = table.id
    user.save()
    return Response({
        "message": "table joined",
        "table_id": table.id,
        "party_size": table.party_size
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def delete_table(request):
    try:
        table = Table.objects.get(owner_id=request.data.get('owner_id'))
    except Table.DoesNotExist:
        return Response({"error":"Table does not exist"}, status=status.HTTP_404_NOT_FOUND)
    table.delete()
    return Response({"result": "table deleted"}, status=status.HTTP_200_OK)

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
    users = MyUser.objects.all().filter(active_table_id=request.data.get('id'))
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def find_server():
    return

