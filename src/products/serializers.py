from django.utils import tree
from rest_framework import serializers
from rest_framework.response import Response
from .models import Table_Product, CartItem, Table_Headers, ItemDevice, Device

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

class DeviceItemSerializer(serializers.ModelSerializer):
    product = TableProductListSerializer(read_only=True)

    class Meta:
        model = ItemDevice
        fields = ('id', 'quantity', 'product')

class DeviceSerializer(serializers.ModelSerializer):
    items = DeviceItemSerializer(read_only=True, many=True)

    class Meta:
        model = Device
        fields = "__all__"
      


