"""
.. Copyright 2012 Cantemo AB. All Rights Reserved
"""

from django.forms import ModelForm
from models import GoogleAnalyticsSettings

# A model form which deferrs everything to the GoogleAnalyticsSettings model
class GoogleAnalyticsForm(ModelForm):
    """ Main form for configuring Google Analytics
    """

    class Meta:
        model = GoogleAnalyticsSettings

