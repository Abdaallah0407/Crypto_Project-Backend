from django.db.models import query
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import SaleItem, Sale
from .serializers import SaleItemSerializer, SaleSerializer
from src.products.models import Table_Product


class APISaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sale.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Sale.objects.filter(user=pk)
        if not queryset:
            return Response([])
        locker = get_object_or_404(queryset, user=pk)
        serializer = SaleSerializer(locker, context={'request': request})
        return Response(serializer.data)


class APIAddSaleItemProduct(generics.CreateAPIView):
    serializer_class = SaleItemSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Sale.objects.all()

    def post(self, request, *args, **kwargs):

        sale, created = Sale.objects.get_or_create(user=request.user)
        product = Table_Product.objects.get(pk=request.data['product'])
        # quantity = int(request.data['quantity'])
        SaleItem.objects.filter(
            sale=sale, product=product)

        sale_item, created = SaleItem.objects.update_or_create(sale=sale, product=product)
        sale_item.save()
        return Response({"Success:Created"}, status=status.HTTP_201_CREATED)




class APIDestroySaleItem(generics.DestroyAPIView):
    serializer_class = SaleItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = SaleItem.objects.all()

    def post(self, request, *args, **kwargs):
        sale, created = Sale.objects.get_or_create(user=request.user)
        sale_item = SaleItem.objects.get(
            sale=sale, product=request.data['product'])
        sale_item.delete()

        c = sale.items.count()
        if c == 0:
            sale.delete()
        return Response({"Success": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
