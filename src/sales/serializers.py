from django.utils import tree
from rest_framework import serializers
from rest_framework.response import Response
from .models import Sale, SaleItem
from products.serializers import ProductListSerializer


class SaleItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = SaleItem
        fields = ("id", "quantity", "product")


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ("id", "user", "items")
