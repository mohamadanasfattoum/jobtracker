from django.shortcuts import render
from .models import JobApplication
from django.views import generic


class JobApplicationListView(generic.ListView):
    model = JobApplication
    context_object_name = "applications"