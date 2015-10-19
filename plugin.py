"""
.. Copyright 2012 Cantemo AB. All Rights Reserved
"""

from portal.pluginbase.core import *
from portal.generic.plugin_interfaces import IPluginURL, IPluginBlock
from django.template import loader, Context
from django.core.exceptions import ObjectDoesNotExist
import logging
log = logging.getLogger(__name__)

# Add extra urls which are defined in urls.py
class AnalyticsPluginURL(Plugin):
    """ Adds extra URLS for the Google Analytics plugin.
    """
    implements(IPluginURL)

    def __init__(self):
        self.name = "Google Analytics Plugin"
        self.urls = 'portal.plugins.GoogleAnalyticsPlugin.urls'
        self.urlpattern = r'^analytics/'
        self.namespace = 'analytics',
        self.plugin_guid = '034A8676-F8B9-4946-BD82-0E78248F84A5'
        log.debug("Initiated AnalyticsPluginURL")

# Register the URL plugin
pluginurls = AnalyticsPluginURL()

# Add the google snippet to each page, via the header_css_js plugin block
class AnalyticsPluginBlock(Plugin):

    implements(IPluginBlock)

    def __init__(self):
        # This is the plugin block we add the plugin output to
        self.name = "header_css_js"
        self.plugin_guid = "7DA4A359-6794-47C7-A18C-4A80330B72D5"
        log.debug("Initiated AnalyticsPluginBlock")

    # Function called by the plugin framework. Returns the rendered template.
    def return_string(self, tagname, *args):
        from models import GoogleAnalyticsSettings
        from django.core.cache import cache
        ret = " "
        google_id = cache.get('google_id')
        if google_id is None:
            # Workaround for django lacking a singleton model. Always access object with id=1
            try:
                obj = GoogleAnalyticsSettings.objects.get(pk=1)
                google_id = obj.google_id
                cache.set('google_id', google_id)
            except ObjectDoesNotExist:
                ret = " "
            else:
                if obj.google_id and obj.google_id != "":
                    ret = 'analytics/google_snippet.html'
        else:
            ret = 'analytics/google_snippet.html'

        return {'guid':self.plugin_guid, 'template': ret, 'context' : {'google_id' : google_id} }

pluginblock = AnalyticsPluginBlock()

# Add an entry to the admin menu
class AnalyticsAdminMenuPlugin(Plugin):

    implements(IPluginBlock)

    def __init__(self):
        # The plugin block to add the menu item to
        self.name = "NavigationAdminPlugin"
        self.plugin_guid = "64993BE2-3FDC-4D75-8374-F6D8B5BABDB4"
        log.debug("Initiated AnalyticsNavigationAdminPlugin")

    # Returns the template file
    def return_string(self, tagname, *args):
        return {'guid':self.plugin_guid, 'template':'analytics/navigation_admin.html' }

pluginblock = AnalyticsAdminMenuPlugin()

class AnalyticsAdminLeftPanePlugin(Plugin):
    """ adds a menu item to the admin screen
    """
    implements(IPluginBlock)

    def __init__(self):
        self.name = "AdminLeftPanelBottomPanePlugin"
        self.plugin_guid = "8B26B086-DD1C-4FF9-84CE-96E6985CE38E"

    def return_string(self, tagname, *args):
        return {'guid': self.plugin_guid, 'template': 'analytics/admin_leftpanel_pane.html'}

pluginblock = AnalyticsAdminLeftPanePlugin()
