from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import APINewsView

router = routers.DefaultRouter()
router.register('api/news', APINewsView, 'news')

urlpatterns = [
    path('', include(router.urls)),
]
