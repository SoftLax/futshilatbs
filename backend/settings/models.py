from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
