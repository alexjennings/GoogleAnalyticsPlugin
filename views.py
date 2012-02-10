"""
.. Copyright 2012 Cantemo AB. All Rights Reserved
"""

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
        # Workaround for django lacking a singleton model. Always access object with id=1
        try:
            obj = GoogleAnalyticsSettings.objects.get(pk=1)
        except ObjectDoesNotExist:
            obj = GoogleAnalyticsSettings(id=1)
            obj.save()

        if self.request.method == 'POST':
            # If this is a POST it means the user pressed submit, so we update the database.
            form = GoogleAnalyticsForm(self.request.POST, instance=obj)
            if form.is_valid(): # All validation rules pass
                ctx['form'] = form
                form.save()
        else:
            # Otherwise we show the form from the database
            ctx['form'] = GoogleAnalyticsForm(instance=obj)

        return self.main(self.request, self.template, ctx)
