from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
        "company_name",
        "job_title",
        "location",
        "job_url",
        "source",
        "application_date",
        "status",
        "notes",
        ]
