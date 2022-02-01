from django.utils import tree
from rest_framework import serializers
from rest_framework.response import Response
from .models import Table_Product, CartItem, Table_Headers

class TableProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table_Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = TableProductListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ("id", "product")


class Table_HeadersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table_Headers
        fields = "__all__"


