from django.db import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from src.abouts.serializers import AboutUsSerializer, OurTeamSerializer


class APIAboutUsView(viewsets.ModelViewSet):
    # queryset = News.objects.all()
    serializer_class = AboutUsSerializer

    def get_queryset(self):
        queryset = AboutUs.objects.order_by('-createdAt')
        return queryset

class APIOurTeamView(viewsets.ModelViewSet):
    # queryset = News.objects.all()
    serializer_class = OurTeamSerializer

    def get_queryset(self):
        queryset = AboutUs.objects.order_by('-createdAt')
        return queryset

