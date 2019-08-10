"""
Forms for Job postings application.
"""
#######################################################################

from django import forms
from django.contrib.staticfiles.storage import staticfiles_storage

from markuphelpers.forms import LinedTextareaWidget, ReStructuredTextFormMixin

from .models import JobPosting

#######################################################################

class AdminJobPostingForm(ReStructuredTextFormMixin, forms.ModelForm):
    """
    A form for the Django admin JobPostings.
    """
    restructuredtext_fields = [ ('content', True), ]
    
    class Meta:
        model = JobPosting
        widgets = {
                'title': forms.TextInput(attrs={'size': 50}),
                'contact_info': LinedTextareaWidget(attrs={'rows': 9}),
                'content': LinedTextareaWidget,
            }
        exclude = []


#######################################################################

class JobPostingForm(AdminJobPostingForm):
    """
    A form for updating JobPostings.
    """
    class Meta(AdminJobPostingForm.Meta):
        fields = ['title', 'deadline', 'slug', 'url', 'where', 
                  'degree_required', 'notes', 'content', ]

    class Media:
        css = {
            'all': (
                    staticfiles_storage.url("css/forms.css"),
                    staticfiles_storage.url("css/twoColumn.css"),
                ),
            }
            
#######################################################################
