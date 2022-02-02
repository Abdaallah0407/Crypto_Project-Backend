# from django import views
from msilib import Table
from operator import index
from turtle import title
from urllib import request
from rest_framework import views
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import CartItem, Table_Product, Table_Headers
from .serializers import CartItemSerializer, Table_HeadersSerializer, TableProductListSerializer




class APICartItemProduct(generics.CreateAPIView):
    queryset = Table_Product.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        queryset = Table_Product.objects.filter(
            pk=request.data['product']).first()
        cart_item, created = CartItem.objects.update_or_create(
            product=queryset)
        cart_item.save()
        return Response({"Success:Created"}, status=status.HTTP_201_CREATED)


class DestroyAPICartItem(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = CartItem.objects.all()

    def post(self, request, *args, **kwargs):
        cart_item = CartItem.objects.get(product=request.data['product'])
        cart_item.delete()

        return Response({"Success": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class APITable_HeadersViewSet(viewsets.ModelViewSet):
    serializer_class = Table_HeadersSerializer

    queryset = Table_Headers.objects.all()



class APITableProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TableProductListSerializer

    queryset = Table_Product.objects.all()


class FillTable(views.APIView):
    def get_queryset(self):
        table_product = Table_Product.objects.all().first()
        countf = table_product.count
        for i in range(2, 61):
            title = "%s M" % (i-1)

            previous_month_product = Table_Product.objects.filter(
                title__contains=title).first()

            totality = previous_month_product.totality + countf

            table_product = Table_Product.objects.update_or_create(
                title="%s M" % i, count=countf, totality=totality, price=0)
        queryset = Table_Product.objects.all()
        return Response(queryset, status=status.HTTP_201_CREATED)


class NextPreviouTable(views.APIView):
    def get_queryset(self):
        queryset = Table_Product.objects.all().order_by('id')
        get_id = self.request.query_params.get('get_id')

        tableprod = Table_Product.objects.get(pk=get_id)
        title = tableprod.title
        title = title.replace(" M", "")
        month = int(title)
        table_prod = Table_Product.objects.filter(
            title__contains="%s M" % str(month+1)).first()
        table_prod.totality = table_prod.count
        table_prod.save()
        counts = table_prod.count
        for i in range(month+2, 61):
            prev_mon_table_prod = Table_Product.objects.filter(
                title__contains="%s M" % str(i-1)).first()
            table_prod = Table_Product.objects.filter(
                title__contains="%s M" % str(i)).first()

            table_prod.totality = prev_mon_table_prod.totality + counts
            table_prod.save()
        tableprod.save()

        return queryset

    # def get_deviceprice(self):
    #     get_id = self.request.query_params.get('get_id')
    #     table_product = Table_Product.objects.get(id=get_id)
    #     mul = table_product.totality * table_product.price
    #     table_product.price_device = mul
    #     table_product.save()
    #     get_deviceprice = Table_Product.objects.filter(id=get_id)
    #     return get_deviceprice

    # serializer_class = TableProductListSerializer


class PriceDevice(viewsets.ModelViewSet):
    def get_queryset(self):
        get_id = self.request.query_params.get('get_id')
        table_product = Table_Product.objects.get(id=get_id)
        mul = table_product.totality * table_product.price
        table_product.price_device = mul
        table_product.save()
        queryset = Table_Product.objects.filter(id=get_id)
        return queryset

    serializer_class = TableProductListSerializer
