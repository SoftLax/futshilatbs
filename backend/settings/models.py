from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FiscalYear(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField(max_length=10)
    end_date = models.DateField(max_length=10)
    is_closed = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
