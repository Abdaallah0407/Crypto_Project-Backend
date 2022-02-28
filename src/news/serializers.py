from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"
