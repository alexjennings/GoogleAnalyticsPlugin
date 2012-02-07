from django.db import models

# Create your models here.

class GoogleAnalyticsSettings(models.Model):
    google_id = models.CharField(max_length=20)
