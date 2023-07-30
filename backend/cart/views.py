from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .models import Cart
from .serializers import CartSerializer

# Create your views here.

# GET
@api_view(['GET'])
def get_all_carts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_cart_by_name(request, pk):
    cart = Cart.objects.filter(name__icontains=pk)
    serializer = CartSerializer(cart, many=True)

    if cart.count() == 0:
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def get_cart_by_cart_items(request, pk):
    cart = Cart.objects.filter(cart_items__contains=[pk])
    serializer = CartSerializer(cart, many=True)

    if cart.count() == 0:
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def get_cart_by_username(request, pk):
    # Determine if user with same username exists
    try:
        user = User.objects.get(username=pk)

        # Determine if there is a cart with that same user
        try:
            cart = Cart.objects.get(created_by=user)
            serializer = CartSerializer(cart, many=False)
        
        # Not found
        except Cart.DoesNotExist:
            return Response("Cart associated with that username doesn't exists.", 
                            status=status.HTTP_404_NOT_FOUND)
        # Found
        else:
            return Response(serializer.data)
    
    # Not found
    except User.DoesNotExist:
        return Response("Username doesn't exists.", 
                        status=status.HTTP_404_NOT_FOUND)

# ADD
@api_view(['POST'])
def create_cart(request):
    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def update_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    serializer = CartSerializer(instance=cart, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def delete_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    deleted_cart = cart

    cart.delete()
    serializer = CartSerializer(deleted_cart, many=False)

    return Response(serializer.data)