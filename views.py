# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from portal.generic.baseviews import ClassView
import logging
log = logging.getLogger(__name__)

from forms import GoogleAnalyticsForm
from models import GoogleAnalyticsSettings
from django.core.exceptions import ObjectDoesNotExist

class GoogleAnalyticsView(ClassView):
    """ Update the settings for the Google Analytics plugin
    """
    def __call__(self):
        log.debug("%s View GoogleAnalyticsView" % self.request.user)
        ctx = {}
        try:
            obj = GoogleAnalyticsSettings.objects.get(pk=1)
        except ObjectDoesNotExist:
            obj = GoogleAnalyticsSettings(id=1)
            obj.save()
            
        if self.request.method == 'POST':
            form = GoogleAnalyticsForm(self.request.POST, instance=obj)
            if form.is_valid(): # All validation rules pass
                ctx['form'] = form
                form.save()
        else:
            ctx['form'] = GoogleAnalyticsForm(instance=obj)


        return self.main(self.request, self.template, ctx)
