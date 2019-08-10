"""
Job Posting admin

"""
import datetime

from django.contrib import admin

from .forms import AdminJobPostingForm
from .models import JobPosting, JobUrl, JobUrlCategory

######################################################################

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'where', 'degree_required', 'deadline',  ]
    list_filter = ['active', 'deadline', 'created', 'modified', ]
    search_fields = ['title', 'where', 'contact_info', 'notes', 'content', ]
    ordering = ['-deadline', ]
    prepopulated_fields = {'slug': ("deadline", "title", )}
    form = AdminJobPostingForm

    def get_queryset(self, request):
        """
        This function restricts the default queryset in the
        admin list view.
        """
        qs = super(JobPostingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(active=True, deadline__gte=datetime.date.today())


admin.site.register(JobPosting, JobPostingAdmin)



######################################################################

class JobUrlCategoryAdmin(admin.ModelAdmin):
    list_filter = ['active', 'created', 'modified', ]


admin.site.register(JobUrlCategory, JobUrlCategoryAdmin)



######################################################################

class JobUrlAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url', ]
    list_filter = ['active', 'category', 'created', 'modified', ]

admin.site.register(JobUrl, JobUrlAdmin)



######################################################################

#
