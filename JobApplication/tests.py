from django.test import TestCase
from django.urls import reverse

from .models import JobApplication


class TestJobApplication(TestCase):
    def setUp(self):
        self.application = JobApplication.objects.create(
            company_name="Blus",
            job_title="Entwickler",
            location="Berlin",
        )

    def test_job_application_can_be_created(self):
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(self.application.company_name, "Blus")
        self.assertEqual(self.application.job_title, "Entwickler")
        self.assertEqual(self.application.location, "Berlin")

    def test_default_status_is_planned(self):
        self.assertEqual(self.application.status, "planned")

    def test_str_returns_company_and_job_title(self):
        self.assertEqual(str(self.application), "Blus - Entwickler")

    def test_application_list_page_returns_status_code_200(self):
        url = reverse("application_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_application_list_page_uses_correct_template(self):
        url = reverse("application_list")
        response = self.client.get(url)

        self.assertTemplateUsed(response, "JobApplication/jobapplication_list.html")

    def test_saved_application_is_displayed_on_list_page(self):
        url = reverse("application_list")
        response = self.client.get(url)

        self.assertContains(response, "Blus")
        self.assertContains(response, "Entwickler")
        self.assertContains(response, "Geplant")


    def test_application_create_page_returns_status_code_200(self):
        url = reverse("application_create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


    def test_application_can_be_created_from_form(self):
        url = reverse("application_create")

        data = {
            "company_name": "FERCHAU",
            "job_title": "Softwareentwickler",
            "location": "Rostock",
            "job_url": "https://example.com/job",
            "source": "LinkedIn",
            "application_date": "2026-07-16",
            "status": "planned",
            "notes": "Test Bewerbung",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(JobApplication.objects.count(), 2)
        self.assertTrue(
            JobApplication.objects.filter(
                company_name="FERCHAU",
                job_title="Softwareentwickler",
            ).exists()
        )

    def test_application_update_page_returns_status_code_200(self):
        url = reverse("application_update", kwargs={"pk": self.application.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


    def test_application_can_be_updated_from_form(self):
        url = reverse("application_update", kwargs={"pk": self.application.pk})

        data = {
            "company_name": "FERCHAU",
            "job_title": "Softwareentwickler",
            "location": "Rostock",
            "job_url": "https://example.com/job",
            "source": "LinkedIn",
            "application_date": "2026-07-16",
            "status": "applied",
            "notes": "Test Bewerbung",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(JobApplication.objects.count(), 1)
        self.application.refresh_from_db()

        self.assertEqual(self.application.company_name, "FERCHAU")
        self.assertEqual(self.application.job_title, "Softwareentwickler")
        self.assertEqual(self.application.location, "Rostock")
        self.assertEqual(self.application.status, "applied")