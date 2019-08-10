"""
Job Postings URLS
"""
from django.conf.urls import url

from .views import JobDetailView, JobListView

urlpatterns = [
    url(r'^$', 
        JobListView.as_view(),
        name="jobpost-list",
        ),
    url('(?P<slug>[\w-]+)/$',
        JobDetailView.as_view(),
        name="jobpost-detail",
        ),
    ]
