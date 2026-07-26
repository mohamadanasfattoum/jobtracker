import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand

from JobApplication.models import JobApplication


class Command(BaseCommand):
    help = "Create mixed dummy job applications for development and testing."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=25,
            help="Number of dummy applications to create.",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing applications before creating dummy data.",
        )

    def handle(self, *args, **options):
        count = options["count"]
        clear = options["clear"]

        if clear:
            JobApplication.objects.all().delete()
            self.stdout.write(self.style.WARNING("Existing applications deleted."))

        companies = [
            "FERCHAU",
            "Friedrich-Loeffler-Institut",
            "Dietrich-Bonhoeffer-Klinikum",
            "Touris Marketing Service GmbH",
            "IT Solutions MV",
            "Nord Software GmbH",
            "Hanse IT Service",
            "Digital MV GmbH",
            "CloudTech Solutions",
            "Backend Factory GmbH",
        ]

        job_titles = [
            "Softwareentwickler",
            "Backend Entwickler",
            "Python Developer",
            "IT-Mitarbeiter",
            "Junior Web Developer",
            "Application Manager",
            "Django Entwickler",
            "Full Stack Developer",
            "Softwaretester",
            "API Developer",
        ]

        locations = [
            "Rostock",
            "Greifswald",
            "Neubrandenburg",
            "Stralsund",
            "Schwerin",
            "Hamburg",
            "Berlin",
            "Remote",
        ]

        sources = [
            "LinkedIn",
            "StepStone",
            "Arbeitsagentur",
            "Karriereportal",
            "Indeed",
            "Unternehmenswebseite",
            "Empfehlung",
        ]

        statuses = [
            "planned",
            "applied",
            "interview",
            "task",
            "rejected",
            "accepted",
        ]

        start_date = date(2026, 7, 1)

        for i in range(count):
            company = random.choice(companies)
            job_title = random.choice(job_titles)
            location = random.choice(locations)
            source = random.choice(sources)
            status = random.choice(statuses)

            random_days = random.randint(0, 60)
            application_date = start_date + timedelta(days=random_days)

            JobApplication.objects.create(
                company_name=company,
                job_title=job_title,
                location=location,
                job_url=f"https://example.com/job-{i + 1}",
                source=source,
                application_date=application_date,
                status=status,
                notes=f"Dummy Bewerbung Nummer {i + 1}",
            )

        self.stdout.write(
            self.style.SUCCESS(f"{count} mixed dummy applications created successfully.")
        )