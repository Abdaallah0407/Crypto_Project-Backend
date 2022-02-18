from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from .serializers import UserSerilaizer
from src.accounts.models import User

# Create your views here.

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerilaizer

    def get_object(self):
        return self.request.user


# class Logout(APIView):

#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)