from rest_framework import generics
from rest_framework import permissions
from .models import Client, FiscalYear
from .serializers import ClientSerializer, FiscalYearSerializer

class ClientList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FiscalYearList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = FiscalYear.objects.all()
    serializer_class = FiscalYearSerializer

class FiscalYearCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = FiscalYear.objects.all()
    serializer_class = FiscalYearSerializer

class FiscalYearUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = FiscalYear.objects.filter()
    serializer_class = FiscalYearSerializer

class FiscalYearDelete(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = FiscalYear.objects.filter()
    serializer_class = FiscalYearSerializer