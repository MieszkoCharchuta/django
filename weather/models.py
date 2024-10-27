from django.db import models
from django.utils import timezone

class WeatherCondition(models.Model):
    area = models.CharField(max_length=10)
    observed_at = models.DateTimeField(default=timezone.now)
    temperature = models.CharField(max_length=10)
    pressure = models.CharField(max_length=10)
