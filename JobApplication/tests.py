from django.test import TestCase
from .models import JobApplication

class TestJobApplication(TestCase):
    def setUp(self):
        self.application = JobApplication.objects.create(company_name="Blus",job_title="Entwickler",location="Berlin")

    def test_job_application_can_be_created(self):
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(self.application.company_name, "Blus")
        self.assertEqual(self.application.job_title, "Entwickler")
        self.assertEqual(self.application.location, "Berlin")

    def test_default_status_is_planned(self):
        self.assertEqual(self.application.status, "planned")

    def test_str_returns_company_and_job_title(self):
        self.assertEqual(str(self.application), "Blus - Entwickler")

