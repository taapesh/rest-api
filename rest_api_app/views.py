from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from rest_api_app.models import Table
from rest_api_app.serializers import TableSerializer


@api_view(['GET', 'POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def table_list(request):
    """
    List all tables, or create a new table.
    """
    if request.method == 'GET':
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def table_detail(request, ownerId):
    """
    Retrieve, update or delete a table.
    """
    try:
        table = Table.objects.get(ownerId=ownerId)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TableSerializer(table)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_table_by_addr(request):
    addr = request.data.get('addr')
    tableNum = request.data.get('tableNum')

    try:
        table = Table.objects.filter(tableNum=tableNum)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TableSerializer(table)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def get_server_tables(request):
    if (request.data.get('finished')):
        tables = Table.objects.filter(serverId=request.data.get('serverId')).filter(isFinished=True)
    elif (request.data.get('requested')):
        tables = Table.objects.filter(serverId=request.data.get('serverId')).filter(requestMade=True)
    else:
        tables = Table.objects.filter(serverId=request.data.get('serverId'))

    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def leave_table(request):
    user = User.objects.get(id=userId)

    try:
        table = Table.objects.get(ownerId=user.currentTableId)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    table.partySize -= 1


@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def make_table_request(request):
    try:
        table = Table.objects.get(ownerId=ownerId);
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    table.requestMade = True
    table.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
def increase_party_count(request):
    try:
        table = Table.objects.get(ownerId=ownerId);
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    table.partySize += 1
    table.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

