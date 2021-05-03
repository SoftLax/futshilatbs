from django.urls import path
from .views import ClientList

app_name = 'settings'

urlpatterns = [
    path('clientlist/', ClientList.as_view(), name='clientlist'),
    #path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
]