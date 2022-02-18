from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import APITableProductUpdateViewSet, SumTable, APITableProductViewSet, APITable_HeadersViewSet, DestroyAPICartItem, APICartItemProduct, FillTable, NextPreviouTable, APIDeviceView, APIDeviceItemProduct, APIDeviceUpdateItem, PreviouTable


router = routers.DefaultRouter()
router.register('next-table', NextPreviouTable, "next")
router.register('previo-table', PreviouTable, "previo")
router.register('table-products', APITableProductViewSet, 'products')
router.register('table-headers', APITable_HeadersViewSet,
                'topik-characteristic')
router.register('device', APIDeviceView, 'device')
router.register('device-item', APIDeviceItemProduct, 'device-item')
router.register('sum-item', SumTable, 'device-item')
router.register('productprice-update',
                APITableProductUpdateViewSet, 'productprice-update')

# router.register('api/update-table', UpdatePriceQuantity,'update')


APIDeviceView

urlpatterns = [
    path('', include(router.urls)),
    path('cart-item_product/', APICartItemProduct.as_view(),
         name="cart-item_product"),
    path('destroy-cart/', DestroyAPICartItem.as_view(), name="destroy-cart"),
    path('fill-table/', FillTable.as_view(), name="destroy-cart"),
    path('device-update/', APIDeviceUpdateItem.as_view(), name="cart-update"),
    # path('api/productprice-update/', APITableProductUpdateViewSet.as_view(), name="productprice-update")

    # path('api/next-table/', NextPreviouTable.as_view(), name="next-cart"),
    # path('api/device-item/', APIDeviceItemProduct.as_view(), name="device-item"),
]
