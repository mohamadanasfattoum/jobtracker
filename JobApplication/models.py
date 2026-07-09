from django.db import models


class JobApplication(models.Model):
    status_werte ={
        "planned":"Geplant",
        "applied":"Beworben",
        "interview":"Gespräch",
        "task":"Aufgabe",
        "rejected":"Absage",
        "accepted":"Zusage"
    }
    company_name = models.CharField(max_length=300)
    job_title = models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    job_url = models.URLField(blank=True)
    source = models.CharField(max_length=100, blank=True)
    application_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_werte)
    notes = models.TextField(max_length=500, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.company_name} - {self.job_title}"