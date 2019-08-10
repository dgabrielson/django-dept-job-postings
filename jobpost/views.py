"""
Job Postings extends class-based generic views.
"""
import datetime

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import JobPosting, JobUrlCategory

######################################################################

class JobListView(ListView):
    """
    Does a list of jobs, and a list of additional resources.
    """
    queryset = JobPosting.objects.filter(active=True, 
                                  deadline__gte=datetime.date.today())
    context_object_name = 'job_list'
    
    
    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context.update({
            'category_list': JobUrlCategory.objects.filter(active=True),
        })
        return context



######################################################################

class JobDetailView(DetailView):
    """
    A view showing details for a particular job.
    """
    queryset = JobPosting.objects.filter(active=True)
    context_object_name ='job'
    
    
    
######################################################################

#
