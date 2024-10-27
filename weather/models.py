from django.db import models
from django.utils import timezone

class WeatherCondition(models.Model):
    observed_at = models.DateTimeField(default=timezone.now)
    temperature = models.CharField(max_length=10)
    pressure = models.CharField(max_length=10)
