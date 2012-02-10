"""
.. Copyright 2012 Cantemo AB. All Rights Reserved
"""

from django.db import models

# This is the only module in the analytics plugin. We try to use it as
# a singleton module and only ever have one row in the table.

class GoogleAnalyticsSettings(models.Model):
    google_id = models.CharField(max_length=20, null=True)
