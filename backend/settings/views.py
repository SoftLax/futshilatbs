from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Client
from .serializers import ClientSerializer

class ClientList(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
