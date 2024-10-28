from django.db import models
from django.utils import timezone

class WeatherCondition(models.Model):
    area = models.CharField(max_length=10, default="Unknown")
    observed_at = models.DateTimeField(default=timezone.now)
    temperature = models.CharField(max_length=10, default="Unknown")
    pressure = models.CharField(max_length=10, default="Unknown")
