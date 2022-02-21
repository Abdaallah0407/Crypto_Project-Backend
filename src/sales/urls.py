from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import APISaleViewSet, APIAddSaleItemProduct, APIDestroySaleItem


router = routers.DefaultRouter()
router.register('api/sale', APISaleViewSet, "sale")

urlpatterns = [
    path('', include(router.urls)),
    path('api/add-sale/', APIAddSaleItemProduct.as_view(),
         name="add-sale"),
    path('api/destroy-sale/', APIDestroySaleItem.as_view(), name="destroy-sale"),
]