from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = "__all__"


class OurTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Our_team
        fields = "__all__"
