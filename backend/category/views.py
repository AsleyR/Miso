from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category
from .serializers import CategorySerializer

# Create your views here.

# GET
@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_category_by_name(request, pk):
    category = Category.objects.filter(name__icontains=pk)
    serializer = CategorySerializer(category, many=True)

    if category.count() == 0:
        return Response(f"Category with name {pk} doesn't exists.",
                        status=status.HTTP_404_NOT_FOUND)
    
    return Response(serializer.data)

# ADD
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def update_category(request, pk):
    try:
        category = Category.objects.get(id=pk)

    except Category.DoesNotExist:
        return Response(f"Category with the ID {pk} doesn't exists.", 
                        status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response(f"Category with the ID {pk} doesn't exists.",
                        status=status.HTTP_404_BAD_REQUEST)
    else:
        category.delete()
        return Response("Category deleted succesfully")