"""
.. Copyright 2012 Cantemo AB. All Rights Reserved
"""

from django.conf.urls.defaults import *

# We only have one url in this app
urlpatterns = patterns('portal.plugins.googleanalytics.views',
    url(r'^settings/$', 'GoogleAnalyticsView', kwargs={'template' : 'analytics/settings.html'} , name='analytics_settings'),
)
