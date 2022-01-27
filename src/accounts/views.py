from rest_framework import generics, permissions
from .serializers import UserSerilaizer
from src.accounts.models import User

# Create your views here.

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerilaizer

    def get_object(self):
        return self.request.user