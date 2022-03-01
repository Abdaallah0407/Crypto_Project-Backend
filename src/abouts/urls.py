from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import APIAboutUsView, APIOurTeamView

router = routers.DefaultRouter()
router.register('api/about', APIAboutUsView, 'about')
router.register('api/team', APIOurTeamView, 'team')

urlpatterns = [
    path('', include(router.urls)),
]
