from django.contrib import admin

from .models import JobApplication

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['company_name','job_title','status','application_date','created_at']
    search_fields = ['company_name','job_title','status']
    list_filter = ['status','created_at','application_date','source']

admin.site.register(JobApplication,JobApplicationAdmin)