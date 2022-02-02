from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import APITableProductViewSet, APITable_HeadersViewSet, DestroyAPICartItem, APICartItemProduct, FillTable, NextPreviouTable, PriceDevice, APIDeviceView, APIDeviceItemProduct


router = routers.DefaultRouter()
router.register('api/price-device', PriceDevice, "price")
router.register('api/table-products', APITableProductViewSet, 'products')
router.register('api/table-headers', APITable_HeadersViewSet,
                'topik-characteristic')
router.register('api/device', APIDeviceView,'device')


APIDeviceView

urlpatterns = [
    path('', include(router.urls)),
    path('api/cart-item_product/', APICartItemProduct.as_view(),
         name="cart-item_product"),
    path('api/destroy-cart/', DestroyAPICartItem.as_view(), name="destroy-cart"),
    path('api/fill-table/', FillTable.as_view(), name="destroy-cart"),
    path('api/next-table/', NextPreviouTable.as_view(), name="next-cart"),
    path('api/device-item/', APIDeviceItemProduct.as_view(), name="device-item"),
]
