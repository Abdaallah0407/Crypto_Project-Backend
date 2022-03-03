# from _typeshed import HasFileno
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import *
from .serializers import BackCallSerializer


class BackCallApi(generics.GenericAPIView):
    serializer_class = BackCallSerializer
    queryset = BackCall.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
