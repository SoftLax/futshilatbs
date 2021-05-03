from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

admin.site.register(Client, ClientAdmin)
