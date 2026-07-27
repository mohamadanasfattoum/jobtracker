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

        labels = {
            "company_name": "Firma",
            "job_title": "Stelle",
            "location": "Ort",
            "job_url": "Link zur Stellenanzeige",
            "source": "Quelle",
            "application_date": "Bewerbungsdatum",
            "status": "Status",
            "notes": "Notizen",
        }

        widgets = {
            "application_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4}),
            "job_url": forms.URLInput(
                attrs={"placeholder": "https://example.com/job"}
            ),
        }