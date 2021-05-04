from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include('settings.urls', namespace="settings")),   
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
