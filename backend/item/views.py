from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Item
from .serializers import ItemSerializer

# Create your views here.

# GET
@api_view(['GET'])
def get_all_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_item_by_name(request, pk):
    item = Item.objects.filter(name__icontains=pk)
    serializer = ItemSerializer(item, many=True)

    if item.count() == 0:
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def get_item_by_price(request, pk):
    item = Item.objects.filter(price=pk)
    serializer = ItemSerializer(item, many=True)

    if item.count() == 0:
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def get_item_by_sold_status(request, pk):
    bool_pk = pk.lower() in ['true'] # Determine if pk is valid 'true' str
    item = Item.objects.filter(is_sold=bool_pk)
    serializer = ItemSerializer(item, many=True)

    return Response(serializer.data)

# ADD
@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def update_item(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    deleted_item = item

    item.delete()
    serializer = ItemSerializer(deleted_item, many=False)

    return Response(serializer.data)