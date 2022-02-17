from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import APITableProductUpdateViewSet,SumTable,APITableProductViewSet, APITable_HeadersViewSet, DestroyAPICartItem, APICartItemProduct, FillTable, NextPreviouTable, APIDeviceView, APIDeviceItemProduct, APIDeviceUpdateItem, PreviouTable


router = routers.DefaultRouter()
router.register('api/next-table', NextPreviouTable, "next")
router.register('api/previo-table', PreviouTable, "previo")
router.register('api/table-products', APITableProductViewSet, 'products')
router.register('api/table-headers', APITable_HeadersViewSet,
                'topik-characteristic')
router.register('api/device', APIDeviceView,'device')
router.register('api/device-item', APIDeviceItemProduct,'device-item')
router.register('api/sum-item', SumTable,'device-item')

# router.register('api/update-table', UpdatePriceQuantity,'update')





APIDeviceView

urlpatterns = [
    path('', include(router.urls)),
    path('api/cart-item_product/', APICartItemProduct.as_view(),
         name="cart-item_product"),
    path('api/destroy-cart/', DestroyAPICartItem.as_view(), name="destroy-cart"),
    path('api/fill-table/', FillTable.as_view(), name="destroy-cart"),
    path('api/device-update/', APIDeviceUpdateItem.as_view(), name="cart-update"),
    path('api/productprice-update/', APITableProductUpdateViewSet.as_view(), name="productprice-update")
    
    # path('api/next-table/', NextPreviouTable.as_view(), name="next-cart"),
    # path('api/device-item/', APIDeviceItemProduct.as_view(), name="device-item"),
]
