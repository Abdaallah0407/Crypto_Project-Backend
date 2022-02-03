from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class PaginationProducts(PageNumberPagination):
    page_size = 12
    max_page_size = 1000




    # def get_divice(self):
    #     get_pk = self.request.query_params.get('get_pk')
    #     get_device = self.request.query_params.get('get_device')
    #     table_product = Table_Product.objects.get(id=get_pk)

    #     device_item = ItemDevice.objects.get(id=get_device)

    #     mul = table_product.totality * table_product.price
    #     table_product.price_device = mul

    #     summa = table_product.price_device * device_item.quantity
    #     table_product.price_per_quantity = summa

    #     table_product.save()
    #     get_device = Table_Product.objects.filter(id=get_pk)
    #     return get_device
    # serializer_class = TableProductListSerializer


# class PriceDevice(viewsets.ModelViewSet):
#     def get_queryset(self):
#         get_id = self.request.query_params.get('get_id')
#         get_device = self.request.query_params.get('get_device')
#         table_product = Table_Product.objects.get(id=get_id)

#         device_item = ItemDevice.objects.get(id=get_device)

#         mul = table_product.totality * table_product.price
#         table_product.price_device = mul

#         summa = table_product.price_device * device_item.quantity
#         table_product.price_per_quantity = summa

#         table_product.save()
#         queryset = Table_Product.objects.filter(id=get_id)
#         return queryset
#     serializer_class = TableProductListSerializer
