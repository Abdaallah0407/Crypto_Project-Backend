# from django import views
from urllib import request
from rest_framework import views
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import CartItem, Table_Product, Table_Headers, Device, ItemDevice
from .serializers import CartItemSerializer, Table_HeadersSerializer, TableProductListSerializer, DeviceItemSerializer, DeviceSerializer, TableSumListSerializer
from .service import PaginationProducts
import random


class APIDeviceView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class APIDeviceItemProduct(viewsets.ModelViewSet):
    serializer_class = DeviceItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = ItemDevice.objects.all()

    def post(self, request, *args, **kwargs):

        product = Device.objects.get(pk=request.data['product'])
        quantity = int(request.data['quantity'])
        ItemDevice.objects.filter(
            product=product).update(quantity=quantity)

        device_item = ItemDevice.objects.update_or_create(product=product,
                                                          quantity=quantity)
        device_item.save()
        return Response({"Success:Created"}, status=status.HTTP_201_CREATED)


class APIDeviceUpdateItem(generics.CreateAPIView):
    serializer_class = DeviceItemSerializer
    queryset = ItemDevice.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):

        device_id = request.data['device_item']
        print(device_id)
        product = Device.objects.get(id=device_id)

        device_item = ItemDevice.objects.filter(product=product).first()
        if device_item:
            if 'minus' in self.request.query_params:
                if device_item.quantity > 1:
                    device_item.quantity -= 1
            else:
                device_item.quantity += 1
        else:
            device_item = ItemDevice.objects.create(
                product=product, quantity=2)
        table_products = Table_Product.objects.filter(is_solid=True)
        for table_product in table_products:
            table_product.price_per_quantity = table_product.price_device * device_item.quantity
            table_product.save()
        device_item.save()

        return Response({"Success": "Created"}, status=status.HTTP_201_CREATED)


class APICartItemProduct(generics.CreateAPIView):
    queryset = Table_Product.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        queryset = Table_Product.objects.filter(
            pk=request.data['product']).first()

        tablepsolid = Table_Product.objects.get(pk=request.data['product'])

        is_solid = tablepsolid.is_solid
        if is_solid:
            tablepsolid.is_solid = False
        else:
            tablepsolid.is_solid = True
        tablepsolid.save()
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

        tablepsolid = Table_Product.objects.get(pk=request.data['product'])

        is_solid = tablepsolid.is_solid
        if is_solid:
            tablepsolid.is_solid = False
        else:
            tablepsolid.is_solid = True
        tablepsolid.save()

        cart_item = CartItem.objects.get(product=request.data['product'])
        cart_item.delete()

        return Response({"Success": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class APITable_HeadersViewSet(viewsets.ModelViewSet):
    serializer_class = Table_HeadersSerializer

    queryset = Table_Headers.objects.all()

class APITableProductUpdateViewSet(generics.CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TableProductListSerializer

    def post(self, request, *args, **kwargs):
        table_products = Table_Product.objects.filter(is_solid=True)
        for table_product in table_products:
            table_product.price_device = table_product.totality * table_product.price
            table_product.save()
        return Response({"Success": "Created"}, status=status.HTTP_201_CREATED)


class APITableProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TableProductListSerializer
    pagination_class = PaginationProducts

    def get_queryset(self):
        queryset = Table_Product.objects.order_by('id')

        return queryset


class FillTable(views.APIView):
    def get_queryset(self):
        table_product = Table_Product.objects.all().first()
        countf = table_product.count
        for i in range(2, 61):
            title = "%s M" % (i-1)
            previous_month_product = Table_Product.objects.filter(
                title__contains=title).first()

            totality = previous_month_product.totality + countf

            k = random.randint(10000, 100000)

            mul = totality * k

            table_product = Table_Product.objects.update_or_create(
                title="%s M" % i, count=countf, totality=totality, price=k, price_device=mul)

        queryset = Table_Product.objects.all()
        return Response(queryset, status=status.HTTP_201_CREATED)


class NextPreviouTable(viewsets.ModelViewSet):
    serializer_class = TableProductListSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = Table_Product.objects.all().order_by('id')
        get_id = self.request.query_params.get('get_id')
        device_item = ItemDevice.objects.all().first()

        tableprod = Table_Product.objects.get(pk=get_id)

        summa = tableprod.price_device * device_item.quantity
        tableprod.price_per_quantity = summa
        tableprod.save()

        title = tableprod.title
        title = title.replace(" M", "")
        month = int(title)
        table_prod = Table_Product.objects.filter(
            title__contains="%s M" % str(month+1)).first()
        table_prod.totality = table_prod.count
        table_prod.price_device = table_prod.totality * table_prod.price
        if table_prod.price_per_quantity:
            table_prod.price_per_quantity = table_prod.price_device * device_item.quantity

        table_prod.save()
        if table_prod.is_solid:
            return
        counts = table_prod.count
        for i in range(month+2, 61):
            prev_mon_table_prod = Table_Product.objects.filter(
                title__contains="%s M" % str(i-1)).first()
            table_prod = Table_Product.objects.filter(
                title__contains="%s M" % str(i)).first()

            table_prod.totality = prev_mon_table_prod.totality + counts
            table_prod.price_device = table_prod.totality * table_prod.price
            if table_prod.price_per_quantity:
                table_prod.price_per_quantity = table_prod.price_device * device_item.quantity

            table_prod.save()
            if table_prod.is_solid:
                break
        tableprod.save()

        # get_pk = self.request.query_params.get('get_pk')

        # if item.get('price_per_quantity') != None:

        # mul = table_product.totality * table_product.price
        # table_product.price_device = mul

        return queryset


# class UpdatePriceQuantity(viewsets.ModelViewSet):
#     def get_queryset(self, request, *args, **kwargs):
#         product = Table_Product.objects.all().order_by('id')
#         get_id = self.request.query_params.get('get_id')
#         device_item = ItemDevice.objects.all().first()
#         if device_item:

#             if 'minus' in self.request.query_params:
#                 if device_item.quantity > 1:
#                     device_item.quantity -= 1
#             else:
#                 device_item.quantity += 1

#         tableprod = Table_Product.objects.get(pk=get_id)
#         title = tableprod.title
#         title = title.replace(" M", "")
#         month = int(title)
#         table_prod = Table_Product.objects.filter(
#             title__contains="%s M" % str(month+1)).first()

#         for i in range(month+2, 61):
#             update_month_product = Table_Product.objects.filter(
#                 title__contains=get_id).first()

#             table_prod = update_month_product.price_per_quantity * device_item.quantity

#             table_prod = Table_Product.objects.update_or_create(
#                 title="%s M" % i, price_per_quantity=table_prod)


#         table_prod.save()
#         tableprod.save()


class PreviouTable(viewsets.ModelViewSet):
    serializer_class = TableProductListSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = Table_Product.objects.all().order_by('id')
        get_id = self.request.query_params.get('get_id')
        device_item = ItemDevice.objects.all().first()
        table_prod = Table_Product.objects.get(pk=get_id)
        title = table_prod.title
        title = title.replace(" M", "")
        month = int(title)

        # table_prod = Table_Product.objects.filter(
        #     title__contains="%s M" % str(month)).first()
        # table_prod.totality = table_prod.count
        table_prod.price_device = table_prod.totality * table_prod.price
        if table_prod.price_per_quantity:
            table_prod.price_per_quantity = table_prod.price_device * device_item.quantity

        # table_prod.save()
        counts = table_prod.count
        for i in range(month+1, 61):
            prev_mon_table_prod = Table_Product.objects.filter(
                title__contains="%s M" % str(i-1)).first()
            table = Table_Product.objects.filter(
                title__contains="%s M" % str(i)).first()

            table.totality = prev_mon_table_prod.totality + counts
            table.price_device = table.totality * table.price
            if table.price_per_quantity:
                table.price_per_quantity = table.price_device * device_item.quantity

            # table_prod.price_device = table_prod.totality * table.price

            table.save()
            if table.is_solid:
                break
        # tableprod.save()

        # get_pk = self.request.query_params.get('get_pk')
        # get_device = self.request.query_params.get('get_device')

        table_product = Table_Product.objects.get(id=get_id)

        device_item = ItemDevice.objects.all().first()

        # mul = table_product.totality * table_product.price
        # table_product.price_device = mul

        summa = table_product.price_device * device_item.quantity
        table_product.price_per_quantity = summa

        price_per_quantity = table_product.price_per_quantity

        if price_per_quantity:
            table_product.price_per_quantity = None

        table_product.save()
        # get_device = Table_Product.objects.filter(id=get_id)

        return queryset


# def counter():
#     sum = 0

#     for item in results:
#         if item.get('price_per_quantity') != None:
#             sum = sum+item.get('price_per_quantity')
#     print(sum)
# counter()


class SumTable(viewsets.ModelViewSet):
    serializer_class = TableSumListSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Table_Product.objects.all().order_by('id')

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())

        return total_cost

    # for item in():
    #     if item.get('price_per_quantity') != None:
    #         sum = queryset+item.get('price_per_quantity')

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        print(total_cost)
        return total_cost

    # def create(self):
    #     price_per_quantity = Table_Product.objects.all().order_by('id')
    #     price_quantity = price_per_quantity.price_per_quantity
    #     summa = Table_Product.objects.filter(
    #         price_per_quantity=price_quantity)
    #     for item in ():
    #          if item.get('price_per_quantity') != None:
    #              summa = sum+item.get('price_per_quantity')

    #              summa.save()

    #     return Response(status=status.HTTP_201_CREATED)
