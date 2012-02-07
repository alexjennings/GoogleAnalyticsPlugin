from portal.pluginbase.core import *
from portal.generic.plugin_interfaces import IPluginURL, IPluginBlock
from models import GoogleAnalyticsSettings
import logging
log = logging.getLogger(__name__)

class AnalyticsPluginURL(Plugin):
    """ Adds extra URLS for the testapp plugin.
    """
    implements(IPluginURL)
    
    def __init__(self):
        self.name = "Google Analytics Plugin"
        self.urls = 'portal.plugins.GoogleAnalyticsPlugin.urls'
        self.urlpattern = r'^analytics/'
        self.namespace = 'analytics',
        self.plugin_guid = '034A8676-F8B9-4946-BD82-0E78248F84A5'
        log.debug("Initiated AnalyticsPluginURL")

pluginurls = AnalyticsPluginURL()


class AnalyticsPluginBlock(Plugin):
    
    implements(IPluginBlock)

    def __init__(self):
        self.name = "header_css_js"
        self.plugin_guid = "7DA4A359-6794-47C7-A18C-4A80330B72D5"
        log.debug("Initiated AnalyticsPluginBlock")

    def render_template(self):
        #Test to render a template
        t = loader.get_template('navigation_admin.html')
        c = Context()
        return t.render(c)
        

    def return_string(self, tagname, *args):
        try:
            obj = GoogleAnalyticsSettings.objects.get(pk=1)
        except ObjectDoesNotExist:
            ret = ""
#        else:
#            if obj.google_id and obj.google_id != "":
#                pass

        return {'guid':self.plugin_guid, 'template':'google_snippet.html' }

pluginblock = AnalyticsPluginBlock() 

class AnalyticsNavigationAdminPlugin(Plugin):
    
    implements(IPluginBlock)

    def __init__(self):
        self.name = "AnalyticsNavigationAdminPlugin"
        self.plugin_guid = "64993BE2-3FDC-4D75-8374-F6D8B5BABDB4"
        log.debug("Initiated AnalyticsNavigationAdminPlugin")

    def render_template(self):
        #Test to render a template
        t = loader.get_template('navigation_admin.html')
        c = Context()
        return t.render(c)
        
    def return_string(self, tagname, *args):
        try:
            # Get the given theme
            theme = args[0][2]
        except:
            # fallback to sand theme
            theme = 'sand'
        return {'guid':self.plugin_guid, 'template':'navigation_admin.html' }

pluginblock = AnalyticsNavigationAdminPlugin() 
