from django.urls import path
from .views import ClientList, FiscalYearList, FiscalYearCreate, FiscalYearUpdate, FiscalYearDelete

app_name = 'settings'

urlpatterns = [
    path('clients/', ClientList.as_view()),
    path('fiscalyears', FiscalYearList.as_view()),
    path('fiscalyears/create/', FiscalYearCreate.as_view()),
    path('fiscalyears/update/<int:pk>/', FiscalYearUpdate.as_view()),
    path('fiscalyears/delete/<int:pk>/', FiscalYearDelete.as_view()),
]