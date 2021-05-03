from django.urls import path
from .views import ClientList

app_name = 'settings'

urlpatterns = [
    path('', ClientList.as_view()),    
    #path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
]