#########################################################################

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

#########################################################################

class JobPostConfig(AppConfig):
    name = "jobpost"
    verbose_name = _("Job Postings")

    def ready(self):
        """
        Any app specific startup code, e.g., register signals,
        should go here.
        """

#########################################################################
