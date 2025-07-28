import uuid
from django.db import models

class Car(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    factory_year = models.IntegerField(blank=True, null=True)
    model_yaer = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
