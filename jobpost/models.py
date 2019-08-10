"""
Job Posting models.
"""
######################################################################
from __future__ import print_function, unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

from . import conf

######################################################################

RST_HELP = conf.get('restructuredtext_help')


######################################################################

@python_2_unicode_compatible
class JobPosting(models.Model):

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name='creation time')
    modified = models.DateTimeField(auto_now=True, editable=False,
                                    verbose_name='last modification time')

    title = models.CharField(max_length=200,
                    help_text='The Job Title')
    deadline = models.DateField(
                    help_text='When are applications due?')
    # todo: make this unique_for_{year,month,date}='deadline'; update urls/views.
    slug = models.SlugField(unique=True, max_length=100,
                    help_text='The internal URL portion that the Job Posting will be given.  This must be unique for all job postings.')
    url = models.URLField(blank=True, verbose_name="URL",
                    help_text='An optional link to an external website or PDF.')
    where = models.CharField(max_length=200,
                    help_text='The location of the job.')
    degree_required = models.CharField(max_length=100, blank=True,
                    help_text='The required degree, if any.  E.g., "Ph.D", "M.Sc.", etc.')
    contact_info = models.TextField(blank=True, null=True,
                    help_text='Where to submit applications.  This will be processed as <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">ReStructuredText</a>')
    notes = models.CharField(max_length=200, blank=True,
                    help_text='Any short notes')
    content = models.TextField(
                    help_text='The actual posting.  This will be processed as <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">ReStructuredText</a>.  Do not duplicated the title, deadline, where, etc.')


    class Meta:
        verbose_name = 'Job posting'
        ordering = ['deadline', 'title']


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('jobpost-detail', kwargs={'slug': self.slug,})



######################################################################

# TODO: consider extending both of these with an 'ordering' field.

@python_2_unicode_compatible
class JobUrlCategory(models.Model):

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name='creation time')
    modified = models.DateTimeField(auto_now=True, editable=False,
                                    verbose_name='last modification time')

    slug = models.SlugField(unique=True,
                    help_text='A URL fragment to refer to the category.')
    verbose_name = models.CharField(max_length=200,
                                    help_text='The name of the category.')
    verbose_name_plural = models.CharField(max_length=200,
            help_text='The name of the category, if there is more than one.')
    note = models.TextField(blank=True, help_text=RST_HELP)


    class Meta:
        verbose_name = 'Job URL category'
        verbose_name_plural = 'Job URL categories'
        ordering = ['verbose_name_plural', ]


    def __str__(self):
        return self.verbose_name




######################################################################


class JobUrl_Manager(models.Manager):

    def active(self):
        return self.filter(active=True)



@python_2_unicode_compatible
class JobUrl(models.Model):

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name='creation time')
    modified = models.DateTimeField(auto_now=True, editable=False,
                                    verbose_name='last modification time')

    category = models.ForeignKey(JobUrlCategory, on_delete=models.PROTECT,
                                 limit_choices_to={'active':True})
    title = models.CharField(max_length=200, help_text='The link title.')
    url = models.URLField(help_text='The link target.', verbose_name="URL")
    notes = models.CharField(max_length=200, blank=True,
                             help_text='Any short notes')


    objects = JobUrl_Manager()


    class Meta:
        verbose_name = 'Job URL'
        ordering = ['title', ]


    def __str__(self):
        return self.title + ': ' + self.url



######################################################################
