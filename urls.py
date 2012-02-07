from django.conf.urls.defaults import *

# place app url patterns here

urlpatterns = patterns('portal.plugins.GoogleAnalyticsPlugin.views',
    url(r'^settings/$', 'GoogleAnalyticsView', kwargs={'template' : 'settings.html'} , name='analytics_settings'),
)
