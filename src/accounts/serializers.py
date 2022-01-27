from rest_framework import serializers
from src.accounts.models import User

# User Serializer


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"